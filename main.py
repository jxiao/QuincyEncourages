from wait import *
from send_sms import *
from method import *
from get_events import main

events = main()
#events = [datetime(2019, 9, 7, 13, 43, 10, 0)] #replace with events = main() when api is set up
#number = get_phone_number()
for event in events:
    wait_until_message(event_start_to_datetime(event))
    #message = get_message()
    message = "you're doing great!" #replace with message() once its implemented
    number = "<enter a phone number>" #delete after implementing get_phone_number
    send_message(message, number)



