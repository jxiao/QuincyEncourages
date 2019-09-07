from datetime import datetime
from datetime import timedelta

event = datetime(2019, 9, 7, 12,49, 0, 0)
currentTimeDifference = event - datetime.now() - timedelta(minutes = 10)
print(currentTimeDifference)
print(currentTimeDifference.seconds)