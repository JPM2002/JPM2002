import os, requests, re

# 1) Exchange refresh_token for an access token
resp = requests.post(
    "https://auth.tidal.com/v1/oauth2/token",
    data={
        "grant_type":    "refresh_token",
        "refresh_token": os.getenv("TIDAL_REFRESH_TOKEN"),
        "client_id":     os.getenv("TIDAL_CLIENT_ID"),
        "client_secret": os.getenv("TIDAL_CLIENT_SECRET")
    }
)
access = resp.json().get("access_token", "")

# 2) Get currently‐playing info
resp = requests.get(
    "https://api.tidal.com/v1/me/player/currently-playing",
    headers={"Authorization": f"Bearer {access}"}
)
data = resp.json().get("item", {})

# 3) Build the markdown line
if data:
    title  = data["title"]
    artist = data["artists"][0]["name"]
    now = f"🎧 Now Playing: **{title}** by **{artist}**"
else:
    now = "🎧 Now Playing: _none_"

# 4) Patch your README
with open("README.md", encoding="utf-8") as f:
    text = f.read()

new = re.sub(
    r"<!-- NOW_PLAYING_START -->.*?<!-- NOW_PLAYING_END -->",
    f"<!-- NOW_PLAYING_START -->\n{now}\n<!-- NOW_PLAYING_END -->",
    text,
    flags=re.S
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new)
