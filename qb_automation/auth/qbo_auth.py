import os
import json
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

class QBOAuth:
    def __init__(self, company_id):
        self.company_id = company_id
        self.token_path = f'config/tokens/{self.company_id}_token.json'
        self.auth_client = self._create_auth_client()

    def _create_auth_client(self):
        with open('config/qbo_credentials.json') as f:
            credentials = json.load(f)

        return AuthClient(
            client_id=credentials['client_id'],
            client_secret=credentials['client_secret'],
            redirect_uri=credentials['redirect_uri'],
            environment='sandbox',  # or 'production'
        )

    def get_access_token(self):
        if os.path.exists(self.token_path):
            with open(self.token_path) as f:
                token_data = json.load(f)
            self.auth_client.access_token = token_data['access_token']
            self.auth_client.refresh_token = token_data['refresh_token']
            self.auth_client.realm_id = token_data['realm_id']
            # Refresh the token if it's expired
            self.auth_client.refresh()
            self.save_token()
        else:
            self._get_new_token()

        return self.auth_client

    def _get_new_token(self):
        auth_url = self.auth_client.get_authorization_url([Scopes.ACCOUNTING])
        print(f'Please go to this URL and authorize the app: {auth_url}')
        auth_code = input('Enter the authorization code: ')
        self.auth_client.get_bearer_token(auth_code, realm_id=self.company_id)
        self.save_token()

    def save_token(self):
        token_data = {
            'access_token': self.auth_client.access_token,
            'refresh_token': self.auth_client.refresh_token,
            'realm_id': self.auth_client.realm_id,
        }
        with open(self.token_path, 'w') as f:
            json.dump(token_data, f)

if __name__ == '__main__':
    company_id = input('Enter your company ID: ')
    qbo_auth = QBOAuth(company_id)
    auth_client = qbo_auth.get_access_token()
    print('Access token retrieved successfully.')
