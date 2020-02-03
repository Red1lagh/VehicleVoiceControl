# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACdda95eb0d274c4484e10958b2bfa27de'
auth_token = '6304e59ed76865243c03e491038cb78b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello from GSEII PFA, nod rah mcha lhal",
                     from_='+18304480936',
                     to='+212620828408'
                 )

print(message.sid)
