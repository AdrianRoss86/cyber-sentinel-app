import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the service account
def get_sheet(sheet_name):
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1  # Assumes you're using the first sheet tab
    return sheet

# Log answer data to sheet
def log_response(topic, subtopic, question, answer, correct, notes=""):
    sheet = get_sheet("Cyber Sentinel Study Tracker Template")  # Your sheet name here

    today = datetime.today().strftime('%Y-%m-%d')
    row = [today, topic, subtopic, question, answer, correct, notes]
    sheet.append_row(row)