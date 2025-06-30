from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'calendar_credentials.json', SCOPES
    )
    creds = flow.run_local_server(host='localhost', port=8080, authorization_prompt_message='Please visit this URL: {url}', success_message='Authorization completed. You may close this window.', open_browser=True)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_study_event():
    service = get_calendar_service()

    now = datetime.utcnow()
    start_time = now + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': '🛡️ Cyber Sentinel Study Session',
        'description': 'Sharpening cybersecurity skills with Cyber Sentinel.',
        'start': {
            'dateTime': start_time.isoformat() + 'Z',
            'timeZone': 'America/New_York',  # Adjust if needed
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
            'timeZone': 'America/New_York',
        },
    }

    event_result = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event_result.get('htmlLink')}")

if __name__ == '__main__':
    create_study_event()