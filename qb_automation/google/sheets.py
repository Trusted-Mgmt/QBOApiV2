from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

class GoogleSheets:
    def __init__(self):
        self.creds = self._get_credentials()
        self.service = build('sheets', 'v4', credentials=self.creds)

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

    def get_sheet_data(self, spreadsheet_id, range_name):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                        range=range_name).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            return values
        except HttpError as err:
            print(err)

if __name__ == '__main__':
    sheets = GoogleSheets()
    spreadsheet_id = 'YOUR_SPREADSHEET_ID'  # Please set your spreadsheet ID here
    range_name = 'Sheet1'  # Please set your sheet name here
    data = sheets.get_sheet_data(spreadsheet_id, range_name)
    if data:
        for row in data:
            print(row)
