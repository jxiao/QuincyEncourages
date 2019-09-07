from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACee3a49b44290955782cc35f8b5e7259a'
auth_token = 'ask calvin for this'
client = Client(account_sid, auth_token)

def send_message(message, from_number, to_number): #ask calvin for from number
    message = client.messages \
    .create(
         body= message,
         from_= str(from_number),
         to= str(to_number)
     )
