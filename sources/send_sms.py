# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '*********put your account sid after registring in the API'
auth_token = '*********put your Auth key after registring in the API'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello from GSEII PFA, nod rah mcha lhal",
                     from_='+18304480936',
                     to='+212620828408'
                 )

print(message.sid)
