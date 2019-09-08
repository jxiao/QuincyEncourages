import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from twilio.rest import Client
from datetime import *
import time

import markovify


SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def sendMessage(message, to_number):
    message = client.messages \
    .create(
        body= message,
        from_= "",
        to= str(to_number)
    )

    print("message sent")

def get_message(feeling, sex, school):
    print(feeling + " " + sex + " "+ school)
    if feeling == "boy" and sex == "good":
        # Get raw text as string.
        with open("bgg.txt") as f:
            text = f.read()
        # Build the model.
        text_model = markovify.Text(text)

        return(text_model.make_short_sentence(500))
    if feeling == "girl" and sex == "good":
        # Get raw text as string.
        with open("fgg.txt") as f:
            text = f.read()
        # Build the model.
        text_model = markovify.Text(text)

        return(text_model.make_short_sentence(500))
    if feeling == "girl" and sex == "bad":
        # Get raw text as string.
        with open("fbg.txt") as f:
            text = f.read()
        # Build the model.
        text_model = markovify.Text(text)

        return(text_model.make_short_sentence(500))
    if feeling == "boy" and sex == "bad":
        # Get raw text as string.
        with open("bbg.txt") as f:
            text = f.read()
        # Build the model.
        text_model = markovify.Text(text)

        return(text_model.make_short_sentence(500))

def event_start_to_datetime(event):
    dateTimeString = event['start'].get('dateTime')
    year = int(dateTimeString[0:dateTimeString.find('-')])
    dateTimeString = dateTimeString[dateTimeString.find('-')+1:len(dateTimeString)]
    month = int(dateTimeString[0:2])
    day = int(dateTimeString[3:5])
    hour = int(dateTimeString[6:8])
    minute = int(dateTimeString[9:11])
    second = int(dateTimeString[12:14])
    event_start_datetime = datetime(year, month, day, hour, minute, second)
    return(event_start_datetime)

def wait_until_message(event):
    currentTimeDifference = event - datetime.now()
    if currentTimeDifference.days > 0:
        time.sleep(85799) #sleeps 1 day minus 10 minutes and 1 seconds
        wait_until_message(event)

    if currentTimeDifference.days < 0:
        return
    else:
        secondsUntilMessage = max(0, currentTimeDifference.seconds - 800)
        time.sleep(secondsUntilMessage)

def runitup(events, person):
    for event in events:
        message = get_message(person.sex, person.feeling, person.school)
        print(message)
        wait_until_message(event_start_to_datetime(event))
        number = person.phone_number
        sendMessage(message, number)

def tester(person):
    message = get_message(person.sex, person.feeling, person.school)
    print(message)
    number = person.phone_number
    sendMessage(message, number)
