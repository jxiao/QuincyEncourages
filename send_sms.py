from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACee3a49b44290955782cc35f8b5e7259a'
auth_token = 'f728fd90ae2e5a83d9b05bc0919b1122'
client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='15012616860',
#          to='16466411038'
#      )

# print(message.sid)

def send_message(message, from_number, to_number): #implement this method
    message = client.messages \
    .create(
         body= message,
         from_= str(from_number),
         to= str(to_number)
     )

send_message("asd", 15012616860, 16466411038)