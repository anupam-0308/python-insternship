from twilio.rest import Client

account_sid = "xxxx"    
auth_token = "xxxx" 

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

