import twilio
from twilio.rest import Client


account_sid = "MG389cd9a24cf8ef1ef80945088d038ad4"
auth_token = "6b4912aea689ae24d52a30376b1314d7"
TWILIONUMBER = "‪+13203772421‬"
RECEIVERPHONENUMBER = "‪+917050737117‬"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Hello from Twilio!",
    from_=TWILIONUMBER,
    to=RECEIVERPHONENUMBER
)
print(f"Message sent with SID: {message.sid}")
print("Email and SMS sent successfully!")