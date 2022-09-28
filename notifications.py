import smtplib
from email.message import EmailMessage
import time 

EMAIL_ADDRESS = 'carlperez491@gmail.com' # email of the sender
PASSWORD = 'nfttwqekspouvnnp' # password of the sender
def send_mail(user_email, current_price):
    msg = EmailMessage()
    msg['Subject'] = 'Price Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    msg.set_content(f"The price of the commodity is Ugx. {current_price}")
    
    while True:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, PASSWORD)

            smtp.send_message(msg)
        time.sleep(5*60*60) # notification will be sent every after five hours
print(send_mail('charles.mcw@yahoo.com', 2350.0))


