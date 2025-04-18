import requests
import re
from collections import Counter

# --- Configuration ---
USER = "JPM2002"
BASE_URL = f"https://api.discogs.com/users/{USER}"
HEADERS = {"User-Agent": "JPM2002-Discogs-Stats-Script/1.0"}

# Markers in README.md
MARKERS = {
    "collection":  (r"<!-- DISCOGS_COLLECTION_START -->",  r"<!-- DISCOGS_COLLECTION_END -->"),
    "wantlist":    (r"<!-- DISCOGS_WANTLIST_START -->",    r"<!-- DISCOGS_WANTLIST_END -->"),
    "top_artists": (r"<!-- DISCOGS_TOP_ARTISTS_START -->", r"<!-- DISCOGS_TOP_ARTISTS_END -->"),
    "top_genres":  (r"<!-- DISCOGS_TOP_GENRES_START -->",  r"<!-- DISCOGS_TOP_GENRES_END -->"),
    "table":       (r"<!-- DISCOGS_TABLE_START -->",       r"<!-- DISCOGS_TABLE_END -->"),
}

# --- Fetch basic stats ---
resp = requests.get(f"{BASE_URL}/collection/folders/0/releases?per_page=1", headers=HEADERS)
resp.raise_for_status()
collection_count = resp.json()["pagination"]["items"]

resp2 = requests.get(f"{BASE_URL}/wants?per_page=1", headers=HEADERS)
resp2.raise_for_status()
wantlist_count = resp2.json()["pagination"]["items"]

# --- Fetch releases (up to 100) ---
resp3 = requests.get(f"{BASE_URL}/collection/folders/0/releases?per_page=100", headers=HEADERS)
resp3.raise_for_status()
releases = resp3.json()["releases"]

# --- Compute top artists & genres ---
artists = Counter()
genres = Counter()
for r in releases:
    info = r["basic_information"]
    for a in info.get("artists", []):
        artists[a["name"]] += 1
    for g in info.get("genres", []):
        genres[g] += 1

top5 = artists.most_common(5)
top3_genres = genres.most_common(3)

# --- Read existing README.md ---
with open("README.md", encoding="utf-8") as f:
    content = f.read()

def patch_section(text, key, new_body):
    start, end = MARKERS[key]
    # Match from the start marker through to the end marker:
    pattern = f"{start}.*?{end}"
    # Build the replacement block with new_body in between:
    block   = f"{start}\n{new_body}\n{end}"
    return re.sub(pattern, block, text, flags=re.S)

# --- Build dynamic table row ---
artists_str = ", ".join(f"{n} ({c})" for n, c in top5)
genres_str = ", ".join(f"{n} ({c})" for n, c in top3_genres)

table_md = (
    "| 📦 Collection | 🌟 Wantlist | 🎤 Top Artists           | 🎶 Top Genres          |\n"
    "|:-------------:|:-----------:|:-----------------------:|:----------------------:|\n"
    f"| {collection_count} records | {wantlist_count} records | {artists_str} | {genres_str} |"
)

# --- Patch all sections ---
content = patch_section(content, "collection", f"**Discogs Collection:** {collection_count} records")
content = patch_section(content, "wantlist",   f"**Wantlist:** {wantlist_count} records")
content = patch_section(content, "top_artists", f"**Top Artists:** {artists_str}")
content = patch_section(content, "top_genres",  f"**Top Genres:** {genres_str}")
content = patch_section(content, "table",       table_md)

# --- Write back to README.md ---
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)