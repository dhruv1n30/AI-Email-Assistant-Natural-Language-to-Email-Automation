# gmail_sender.py
import base64
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def send_email(subject, body, to_email, creds: Credentials):
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = to_email
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    return service.users().messages().send(userId="me", body={'raw': raw}).execute()
