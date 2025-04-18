import os, tidalapi

# --- Ensure your Client ID & Secret are available ---
# Either export them in your shell, or hard‑code here for this one run:
os.environ['TIDAL_CLIENT_ID']     = 'your_client_id'
os.environ['TIDAL_CLIENT_SECRET'] = 'your_client_secret'

# If you prefer env vars, in your shell do:
# export TIDAL_CLIENT_ID=your_client_id
# export TIDAL_CLIENT_SECRET=your_client_secret

# --- Start a Tidal session & do the OAuth browser flow ---
session = tidalapi.Session()
session.login_oauth_simple()   # opens your browser; log in and allow access

# --- Print out the refresh token to copy into your .env or GitHub Secret ---
print("TIDAL_REFRESH_TOKEN=" + session.refresh_token)
