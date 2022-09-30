import os
import smtplib
from email.message import EmailMessage
import time 
from dotenv import load_dotenv
load_dotenv()


# Configure your Email
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
email_smtp_server = "smtp.example.com"
email_smtp_port = 587
# Configure End

def send_mail(address, current_price):
    receiver = address 
    msg = EmailMessage()
    msg['Subject'] = 'Price Dropped!'
    msg['From'] = "Amazon Price Tracker"
    msg['To'] = receiver
    msg.set_content(f"The price of the commodity is USD. {current_price}")
    
    while True:
        with smtplib.SMTP_SSL(email_smtp_server, email_smtp_server) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)
        time.sleep(2*60*60) # notifications every after 2 hours
        return send_mail

    


