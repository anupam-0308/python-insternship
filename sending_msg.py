from twilio.rest import Clie

account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 

TWILIO_NUMBER = "+13203772421"        
RECEIVER_PHONENUMBER = "+917050737117"  

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio!",
    from_=TWILIO_NUMBER,
    to=RECEIVER_PHONENUMBER
)

print("Message sent with SID:", message.sid)
print("SMS sent successfully!")
