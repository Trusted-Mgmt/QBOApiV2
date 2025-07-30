from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

class GoogleDrive:
    def __init__(self):
        self.creds = self._get_credentials()
        self.service = build('drive', 'v3', credentials=self.creds)

    def _get_credentials(self):
        creds = None
        if os.path.exists('config/tokens/google_token.json'):
            creds = Credentials.from_authorized_user_file('config/tokens/google_token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'config/google_credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('config/tokens/google_token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    def list_files(self, folder_id):
        try:
            results = self.service.files().list(
                q=f"'{folder_id}' in parents", pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        except HttpError as error:
            print(f'An error occurred: {error}')

    def download_file(self, file_id, file_path):
        try:
            request = self.service.files().get_media(fileId=file_id)
            with open(file_path, 'wb') as f:
                f.write(request.execute())
        except HttpError as error:
            print(f'An error occurred: {error}')

if __name__ == '__main__':
    drive = GoogleDrive()
    folder_id = 'YOUR_FOLDER_ID'  # Please set your folder ID here
    drive.list_files(folder_id)
