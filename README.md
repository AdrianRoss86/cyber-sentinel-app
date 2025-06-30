# 🛡️ Cyber Sentinel  
*A Streamlit-powered cybersecurity study companion by Rossovic Group*

Cyber Sentinel is an interactive training app designed to help users strengthen their cybersecurity knowledge through guided study sessions. Featuring a dynamic quiz interface, real-time performance logging, and calendar-integrated study scheduling, this agent embodies the utility of personal automation and AI tooling in education.

---

## 🚀 Features

- 🎓 Engaging multiple-choice study sessions
- 📝 Automatic logging of responses to Google Sheets
- 📊 Performance tracking dashboard (Google Sheets)
- 📆 Study session scheduling via Google Calendar
- 🧠 Built with modular Python and Streamlit

---

## 📂 Project Structure

| File | Purpose |
|------|---------|
| `app.py` | Streamlit front-end interface and quiz logic |
| `google_sheets.py` | Handles logging quiz results to Google Sheets |
| `google_calendar.py` | Schedules study sessions via Google Calendar API |
| `credentials.json` | OAuth credentials for Sheets (excluded from repo) |
| `calendar_credentials.json` | OAuth credentials for Calendar (excluded from repo) |

---

## ⚙️ Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/AdrianRoss86/cyber-sentinel-app.git
   cd cyber-sentinel-app
