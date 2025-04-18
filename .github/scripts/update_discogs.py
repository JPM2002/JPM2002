import requests
import re
from collections import Counter

# --- Configuration ---
USER = "JPM2002"
BASE_URL = f"https://api.discogs.com/users/{USER}"
HEADERS = {"User-Agent": "JPM2002-Discogs-Stats-Script/1.0"}

# Markers in README.md
MARKERS = {
    "collection": (r"<!-- DISCOGS_COLLECTION_START -->", r"<!-- DISCOGS_COLLECTION_END -->"),
    "wantlist":   (r"<!-- DISCOGS_WANTLIST_START -->",   r"<!-- DISCOGS_WANTLIST_END -->"),
    "top_artists":(r"<!-- DISCOGS_TOP_ARTISTS_START -->",r"<!-- DISCOGS_TOP_ARTISTS_END -->"),
    "top_genres": (r"<!-- DISCOGS_TOP_GENRES_START -->", r"<!-- DISCOGS_TOP_GENRES_END -->"),
}

# --- Fetch collection count ---
resp = requests.get(f"{BASE_URL}/collection/folders/0/releases?per_page=1", headers=HEADERS)
resp.raise_for_status()
collection_count = resp.json()["pagination"]["items"]

# --- Fetch wantlist count ---
r2 = requests.get(f"{BASE_URL}/wants?per_page=1", headers=HEADERS)
r2.raise_for_status()
wantlist_count = r2.json()["pagination"]["items"]

# --- Fetch up to 100 releases for deeper stats ---
resp3 = requests.get(f"{BASE_URL}/collection/folders/0/releases?per_page=100", headers=HEADERS)
resp3.raise_for_status()
data = resp3.json()["releases"]

# --- Compute top 5 artists ---
artists = Counter()
for r in data:
    for a in r["basic_information"]["artists"]:
        artists[a["name"]] += 1
top5 = artists.most_common(5)

# --- Compute top 3 genres ---
genres = Counter()
for r in data:
    for g in r["basic_information"]["genres"]:
        genres[g] += 1
top_genres = genres.most_common(3)

# --- Read README.md ---
with open("README.md", encoding="utf-8") as f:
    content = f.read()

# --- Helper to patch a section ---
def patch_section(text, key, new_body):
    start, end = MARKERS[key]
    pattern = f"{start}.*?{end}"
    block = f"{start}\n{new_body}\n{end}"
    return re.sub(pattern, block, text, flags=re.S)

# --- Build new blocks ---
content = patch_section(
    content, "collection",
    f"**Discogs Collection:** {collection_count} records"
)

content = patch_section(
    content, "wantlist",
    f"**Wantlist:** {wantlist_count} records"
)

artists_str = ", ".join(f"{name} ({count})" for name, count in top5)
content = patch_section(
    content, "top_artists",
    f"**Top Artists:** {artists_str}"
)

genres_str = ", ".join(f"{name} ({count})" for name, count in top_genres)
content = patch_section(
    content, "top_genres",
    f"**Top Genres:** {genres_str}"
)

# --- Write back README.md ---
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)