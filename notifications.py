load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# retrieving keys and adding them to the project
# from the .env file through their key names

SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')
PASSWORD = os.getenv('PASSWORD')

def send_mail(user_email, current_price):
    msg = EmailMessage()
    msg['Subject'] = 'Price Alert! - Amazon' 
    msg['From'] = SENDER_ADDRESS
    msg['To'] = user_email
    msg.set_content(f"The price of the commodity is Ugx. {current_price}")
    
    while True:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_ADDRESS, PASSWORD)

            smtp.send_message(msg)
        time.sleep(5*60*60) # notification will be sent every after five hours


