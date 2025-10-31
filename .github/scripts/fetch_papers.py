#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import time
import urllib.parse
from datetime import datetime, timedelta, timezone

import feedparser
import requests
from dateutil import parser as dateparse

README_PATH = "README.md"
START_MARK = "<!-- SOTA-START -->"
END_MARK = "<!-- SOTA-END -->"

# ---- Config via env ----
SEARCH_QUERY = os.getenv("SEARCH_QUERY", 'diffusion OR "large language model"')
ARXIV_CATEGORIES = os.getenv("ARXIV_CATEGORIES", "cs.LG,cs.AI,cs.CV,cs.CL,stat.ML")
DAYS_BACK = int(os.getenv("DAYS_BACK", "2"))
MAX_PAPERS = int(os.getenv("MAX_PAPERS", "10"))

# Twitter/X (optional but enabled in your workflow if secrets/vars exist)
TW_BEARER = os.getenv("TW_BEARER", "").strip()
TW_ACCOUNTS = [s.strip() for s in os.getenv("TW_ACCOUNTS", "").split(",") if s.strip()]

def human_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")

def arxiv_pdf_link(entry) -> str:
    """Prefer direct PDF if present; otherwise build from arXiv ID."""
    for link in entry.get("links", []):
        if link.get("type") == "application/pdf":
            return link.get("href")
    arxiv_id = entry.get("id", "").rsplit("/", 1)[-1]
    if arxiv_id:
        arxiv_id_nover = re.sub(r"v\d+$", "", arxiv_id)  # drop version for stability
        return f"https://arxiv.org/pdf/{arxiv_id_nover}.pdf"
    return entry.get("link", "")

def arxiv_primary_cat(entry) -> str:
    try:
        return entry.get("arxiv_primary_category", {}).get("term", "")
    except Exception:
        return ""

def arxiv_query(search_query: str, categories: list, max_results: int = 20):
    # Combine category ORs with a free-text query (search 'all:' field)
    cat_clause = " OR ".join([f"cat:{c}" for c in categories])
    q = f"({cat_clause}) AND all:{search_query}"
    params = {
        "search_query": q,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    return "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)

def fetch_arxiv_recent(search_query: str, arxiv_categories: str, days_back: int, limit: int):
    categories = [c.strip() for c in arxiv_categories.split(",") if c.strip()]
    url = arxiv_query(search_query, categories, max_results=max(50, limit * 3))
    feed = feedparser.parse(url)

    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    items = []
    for entry in feed.entries:
        dt = dateparse.parse(entry.get("updated", entry.get("published")))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        if dt < cutoff:
            continue

        title = re.sub(r"\s+", " ", entry.get("title", "").strip())
        authors = ", ".join([a.name for a in entry.get("authors", [])]) if entry.get("authors") else ""
        pdf = arxiv_pdf_link(entry)
        primary = arxiv_primary_cat(entry)
        arxiv_abs = entry.get("link", "")

        items.append({
            "title": title,
            "authors": authors,
            "date": human_date(dt),
            "pdf": pdf,
            "abs": arxiv_abs,
            "primary": primary,
        })
        if len(items) >= limit:
            break

    return items

def twitter_headers():
    return {"Authorization": f"Bearer {TW_BEARER}"} if TW_BEARER else {}

def twitter_get(url, params=None, timeout=20):
    """Simple wrapper with basic rate-limit handling."""
    headers = twitter_headers()
    if not headers:
        return None
    resp = requests.get(url, headers=headers, params=params or {}, timeout=timeout)
    if resp.status_code == 429:
        # crude backoff
        time.sleep(5)
        resp = requests.get(url, headers=headers, params=params or {}, timeout=timeout)
    if resp.status_code >= 400:
        return None
    return resp.json()

def twitter_user_id(username: str) -> str:
    data = twitter_get(f"https://api.twitter.com/2/users/by/username/{username}")
    if not data:
        return ""
    return data.get("data", {}).get("id", "")

def twitter_recent_tweets(uid: str, max_results: int = 50):
    data = twitter_get(
        f"https://api.twitter.com/2/users/{uid}/tweets",
        params={"tweet.fields": "created_at", "max_results": str(max_results)},
    )
    if not data:
        return []
    return data.get("data", []) or []

def extract_arxiv_links(text: str):
    return re.findall(r"https?://arxiv\.org/\S+", text or "")

def maybe_fetch_x_links():
    """Return list of {'tweeted_by','url','date'} for arXiv links seen in last DAYS_BACK days."""
    if not (TW_BEARER and TW_ACCOUNTS):
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)
    found = []
    for handle in TW_ACCOUNTS:
        try:
            uid = twitter_user_id(handle)
            if not uid:
                continue
            for tw in twitter_recent_tweets(uid, max_results=50):
                dt = dateparse.parse(tw.get("created_at", "")) if tw.get("created_at") else None
                if dt and dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt and dt < cutoff:
                    continue
                for url in extract_arxiv_links(tw.get("text", "")):
                    found.append({"tweeted_by": handle, "url": url, "date": human_date(dt) if dt else ""})
        except Exception:
            continue

    # Deduplicate by URL
    uniq, seen = [], set()
    for f in found:
        if f["url"] in seen:
            continue
        seen.add(f["url"])
        uniq.append(f)
    return uniq

def render_markdown(papers, xlinks):
    """
    Render a compact table with a 'last updated' line.
    Authors go in <sub> to keep the table tidy.
    """
    from datetime import datetime, timezone

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    header = (
        f"**Topic:** `{SEARCH_QUERY}` • **Categories:** `{ARXIV_CATEGORIES}` "
        f"• **Window:** last {DAYS_BACK} day(s) • **Max:** {MAX_PAPERS}  \n"
        f"_Last updated: {now_utc}_\n\n"
    )

    lines = [header]

    if papers:
        lines.append("| # | Title | Cat. | Date | Links |")
        lines.append("|:-:|:------|:----:|:----:|:------|")
        for i, p in enumerate(papers, 1):
            title = p["title"]
            authors = p["authors"]
            primary = p["primary"] or "—"
            date = p["date"]
            pdf = p["pdf"]
            abs_url = p["abs"]
            # put authors in small text under the title to keep the row short
            title_cell = f"**[{title}]({pdf})**<br><sub>{authors}</sub>" if authors else f"**[{title}]({pdf})**"
            links_cell = f"[pdf]({pdf}) · [abs]({abs_url})"
            lines.append(f"| {i} | {title_cell} | {primary} | {date} | {links_cell} |")

    if xlinks:
        lines.append("\n<details><summary>🔎 Also spotted on X (arXiv links)</summary>\n")
        for xl in xlinks[:10]:
            lines.append(f"- {xl['date']}: {xl['url']} (via @{xl['tweeted_by']})")
        lines.append("\n</details>")

    if not papers and not xlinks:
        lines.append("_No new results in the chosen window._")

    return "\n".join(lines)


def main():
    print(f"[info] Query='{SEARCH_QUERY}', categories='{ARXIV_CATEGORIES}', days_back={DAYS_BACK}, max_papers={MAX_PAPERS}")
    papers = fetch_arxiv_recent(SEARCH_QUERY, ARXIV_CATEGORIES, DAYS_BACK, MAX_PAPERS)
    xlinks = maybe_fetch_x_links()
    block = render_markdown(papers, xlinks)
    update_readme(block)

if __name__ == "__main__":
    main()
