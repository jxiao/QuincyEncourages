from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACee3a49b44290955782cc35f8b5e7259a'
auth_token = '54ac1cdb1a27c54e74c2a06e29d5c4dc'
client = Client(account_sid, auth_token)

def send_message(message, to_number): 
    message = client.messages \
    .create(
         body= message,
         from_= "15012616860",
         to= str(to_number)
     )
