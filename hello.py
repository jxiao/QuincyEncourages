from flask import Flask, render_template
from flask import request
from main import runitup, tester
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'

app = Flask(__name__)

@app.route("/",  methods=["GET","POST"])
def home():
    if request.method == "POST":
        fname = request.form.get("fname", False)
        lname = request.form.get("lname", False)
        phone_number = request.form.get("phone_number", False)
        sex = request.form.get("sex", False)
        feeling = request.form.get("feeling", False)
        school = request.form.get("school", False)
        user = Person(fname, lname, phone_number, sex, feeling, school)
        if user != None:
            tester(user)
        #getEvents(user)
    return render_template("index.html")

@app.route("/action_page.php")
def action_page():
    return render_template("action_page.php.html")

def get_calendar_service(name):
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists(name + '.pickle'):
       with open(name + '.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)

       # Save the credentials for the next run
       with open(name + '.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service

def getEvents(user):
    service = get_calendar_service(user.fname+user.lname)
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of events')
    events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
    event_list = events_result.get('items', [])
    print(event_list)
    runitup(event_list, user)

class Person:
  def __init__(self, fname, lname, phone_number, sex, feeling, school):
    self.fname = fname
    self.lname = lname
    self.phone_number = phone_number
    self.sex = sex
    self.feeling = feeling
    self.school = school

if __name__ == "__main__":
    app.run(debug=True)