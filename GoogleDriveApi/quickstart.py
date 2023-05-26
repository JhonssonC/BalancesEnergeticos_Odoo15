import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./token.json'):
        creds = Credentials.from_authorized_user_file('./token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(
                './credential_sample.json', scopes=['https://www.googleapis.com/auth/drive'], redirect_uri='urn:ietf:wg:oauth:2.0:oob')
            # Tell the user to go to the authorization URL.
            auth_url, _ = flow.authorization_url(prompt='consent')

            print('Please go to this URL: {}'.format(auth_url))

            # The user will get an authorization code. This code is used to get the
            # access token.
            code = input('Enter the authorization code: ')
            
            flow.fetch_token(code=code)

            # You can use flow.credentials, or you can just get a requests session
            # using flow.authorized_session.
            session = flow.authorized_session()
            print (session)
            
            creds = flow.credentials
            
        
        # Save the credentials for the next run
        with open('./token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()