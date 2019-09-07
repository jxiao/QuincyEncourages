from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACee3a49b44290955782cc35f8b5e7259a'
auth_token = 'fe7e9e713974c4adf0490ea59761889c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='<calvin has the number',
         to='enter number here'
     )

print(message.sid)