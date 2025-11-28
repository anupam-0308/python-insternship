import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "beinganupam.rky@gmail.com"
APP_PASSWORD = " jzic bvzv leqk ktet "
RECEIVER = "ayushakabewakoof@gmail.com"

msg = EmailMessage()
msg["FROM"] = EMAIL
msg["TO"] = RECEIVER
msg["SUBJECT"] = "Hello Buddy"

msg.set_content("This email was shared by Python code...")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, RECEIVER, msg.as_string())