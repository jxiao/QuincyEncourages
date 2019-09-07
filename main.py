from wait import *
from send_sms import *
from method import *
from get_events import main

events = main()
#number = get_phone_number()
for event in events:
    wait_until_message(event_start_to_datetime(event))
    #message = get_message()
    message = "you're doing great!" #replace with message() once its implemented
    number = "<enter a phone number>" #delete after implementing get_phone_number
    send_message(message, number)



