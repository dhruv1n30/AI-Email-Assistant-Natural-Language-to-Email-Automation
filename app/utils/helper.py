# General utility functions
import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def get_credentials():
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            return pickle.load(token)

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    return creds
