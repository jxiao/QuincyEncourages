from datetime import datetime
from datetime import timedelta
import time

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
