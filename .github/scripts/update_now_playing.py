import tidalapi
import re

# --- Authenticate with Tidal via browser‑flow (once locally) ---
session = tidalapi.Session()
session.login_oauth_simple()     # pops open the OAuth flow, writes a cache file

# --- Fetch current track ---
player = tidalapi.playback.Player(session)
track = player.current_track()
if track:
    artists = ', '.join(a.name for a in track.artists)
    now_line = f"🎧 Now Playing: **{track.name}** by **{artists}**"
else:
    now_line = "🎧 Now Playing: _none_"

# --- Read & patch README.md ---
with open("README.md", encoding="utf-8") as f:
    text = f.read()

new_text = re.sub(
    r"<!-- NOW_PLAYING_START -->.*?<!-- NOW_PLAYING_END -->",
    f"<!-- NOW_PLAYING_START -->\n{now_line}\n<!-- NOW_PLAYING_END -->",
    text,
    flags=re.S
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_text)
