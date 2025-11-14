from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from urllib.parse import urlparse, parse_qs
import os

CLIENT_SECRET_FILE = 'client_secret.json'
TOKEN_FILE = 'token.json'
SCOPES = ['https://www.googleapis.com/auth/drive.file']

creds = None
if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        flow.redirect_uri = 'http://localhost' #should be same as on token file.
        auth_url, _ = flow.authorization_url(prompt='consent')
        print("Go to the URL and authorize the app:\n", auth_url)

        user_input = input("Paste the full redirect URL: ").strip()

        # Check if it's a full URL or just the code
        if user_input.startswith('http'):
            # Parse the URL to extract the code
            parsed = urlparse(user_input)
            code = parse_qs(parsed.query).get('code', [None])[0]
            if not code:
                raise ValueError("No code found in URL")
        else:
            # Assume it's just the code
            code = user_input

        flow.fetch_token(code=code)
        creds = flow.credentials

    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())

print(f"✅ Authentication successful!. Token file written as {TOKEN_FILE} ")