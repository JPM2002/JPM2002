import requests
import re
from collections import Counter

# --- Configuration ---
USER = "JPM2002"
BASE_URL = f"https://api.discogs.com/users/{USER}"
HEADERS = {"User-Agent": "JPM2002-Discogs-Stats-Script/1.0"}

# Markers in README.md
MARKERS = {
    "collection":      (r"<!-- DISCOGS_COLLECTION_START -->",    r"<!-- DISCOGS_COLLECTION_END -->"),
    "wantlist":        (r"<!-- DISCOGS_WANTLIST_START -->",      r"<!-- DISCOGS_WANTLIST_END -->"),
    "top_artists":     (r"<!-- DISCOGS_TOP_ARTISTS_START -->",   r"<!-- DISCOGS_TOP_ARTISTS_END -->"),
    "top_genres":      (r"<!-- DISCOGS_TOP_GENRES_START -->",    r"<!-- DISCOGS_TOP_GENRES_END -->"),
    "collection_value":(r"<!-- DISCOGS_VALUE_START -->",          r"<!-- DISCOGS_VALUE_END -->"),
}

# --- Fetch counts and stats ---
# Collection count
resp = requests.get(f"{BASE_URL}/collection/folders/0/releases?per_page=1", headers=HEADERS)
resp.raise_for_status()
collection_count = resp.json()["pagination"]["items"]

# Wantlist count
r2 = requests.get(f"{BASE_URL}/wants?per_page=1", headers=HEADERS)
r2.raise_for_status()
wantlist_count = r2.json()["pagination"]["items"]

# Releases data for stats and value
data_url = f"{BASE_URL}/collection/folders/0/releases?per_page=100"
resp3 = requests.get(data_url, headers=HEADERS)
resp3.raise_for_status()
releases = resp3.json()["releases"]

# Top 5 artists
artists = Counter()
for r in releases:
    for a in r["basic_information"]["artists"]:
        artists[a["name"]] += 1
top5 = artists.most_common(5)

# Top 3 genres
genres = Counter()
for r in releases:
    for g in r["basic_information"]["genres"]:
        genres[g] += 1
top_genres = genres.most_common(3)

# Estimated collection value
total_val = sum(
    r["basic_information"].get("lowest_price", 0) for r in releases
)

# Read README
with open("README.md", encoding="utf-8") as f:
    content = f.read()

# Helper to patch sections
def patch_section(text, key, new_body):
    start, end = MARKERS[key]
    pattern = f"{start}.*?{end}"
    block = f"{start}\n{new_body}\n{end}"
    return re.sub(pattern, block, text, flags=re.S)

# Patch each section
content = patch_section(
    content, "collection",
    f"**Discogs Collection:** {collection_count} records"
)
content = patch_section(
    content, "wantlist",
    f"**Wantlist:** {wantlist_count} records"
)
content = patch_section(
    content, "top_artists",
    f"**Top Artists:** {', '.join(f'{n} ({c})' for n, c in top5)}"
)
content = patch_section(
    content, "top_genres",
    f"**Top Genres:** {', '.join(f'{n} ({c})' for n, c in top_genres)}"
)
content = patch_section(
    content, "collection_value",
    f"**Est. Value:** ${total_val:.2f}"
)

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)