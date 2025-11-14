from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

TOKEN_FILE = 'token.json'
#TODO update file to upload and the folder id
FILE_TO_UPLOAD = 'example.zip' #can be path to file
REMOTE_FILE_NAME='example.zip' #how to name file on google drive
FOLDER_ID = '1P_FXOvPvdSAn4_Ho7Qxxxxx' # Gotten from Google drive url of folder

# Load credentials
creds = Credentials.from_authorized_user_file(TOKEN_FILE)

# Build the Drive service
service = build('drive', 'v3', credentials=creds)

# File metadata
file_metadata = {
    'name': REMOTE_FILE_NAME,
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