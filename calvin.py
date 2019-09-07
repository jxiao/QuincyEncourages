import datetime
import time
from datetime import timedelta

def wait_and_message(event):
    currentTimeDifference = event - datetime.datetime.now()
    timeUntilMessage = currentTimeDifference - timedelta(minutes = 10)
    time.sleep(timeUntilMessage)

print("a")