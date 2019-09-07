from datetime import *

def get_message():
    NotImplementedError


def get_phone_number():
    NotImplementedError


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