from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACcff96dfe385b8a4a0170696c64492cf7'
auth_token = 'a5a52855191484d363ff50282e4ec712'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+19084849818',
                              to='+19739065698'
                          )

print(message.sid)