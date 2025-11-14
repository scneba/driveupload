from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

TOKEN_FILE = 'token.json'
FILE_TO_UPLOAD = 'example.zip' #can be path to file
FOLDER_ID = '1P_FXOvPvdSAn4_Ho7QPxxxxxxxxxxf' # get folder id google folder url

# Load credentials
creds = Credentials.from_authorized_user_file(TOKEN_FILE)

# Build the Drive service
service = build('drive', 'v3', credentials=creds)

# File metadata
file_metadata = {
    'name': FILE_TO_UPLOAD,
    'parents': [FOLDER_ID]
}

# Upload the file
media = MediaFileUpload(FILE_TO_UPLOAD, resumable=True)

print(f"Uploading {FILE_TO_UPLOAD}...")

file = service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id, name, webViewLink'
).execute()

print(f"Upload successful!")
print(f"File Name: {file.get('name')}")
print(f"File ID: {file.get('id')}")
print(f"View Link: {file.get('webViewLink')}")