
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

# retrieving keys and adding them to the project
# from the .env file through their key names

# Configure your Email
email_address = "example@example.com"
email_password = "ExamplePassword"
email_smtp_server = "smtp.example.com"
email_smtp_port = 587
# Configure End

def send_email(address,content):
    reciever = address
    msg = MIMEMultipart("alternative")
    msg['From'] = "Amamzon Price Tracker"
    msg['To'] = reciever
    msg['Subject'] = "Price Dropped!"

    data = ""
    for i in content:
        for key in i.keys():
            if key == 'URL':
                # data += "<p style='font-family: sans-serif; font-size: 10px; font-weight: normal; margin: 0; margin-bottom: 5px;'>"+key+"</p>"
                data += "<a style='background-color:#29b6f6; color:white; font-size:16px; text-align:center; padding: .375rem .75rem; width:100vw; border-radius:10px; text-decoration:none' href='"+i[key]+"'>Click to view product</a>"
            else:
                data += "<p style='font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 5px;'>"+key+"</p>"
                data += "<p style='font-family: sans-serif; font-size: 20px; font-weight: 800; margin: 0; margin-bottom: 15px;'>"+i[key]+"</p> "
    html = "<html><head><meta name='viewport' content='width=device-width'> <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'> <title>Simple Transactional Email</title> <style> /* ------------------------------------- INLINED WITH htmlemail.io/inline ------------------------------------- */ /* ------------------------------------- RESPONSIVE AND MOBILE FRIENDLY STYLES ------------------------------------- */ @media only screen and (max-width: 620px) { table[class=body] h1 { font-size: 28px !important; margin-bottom: 10px !important; } table[class=body] p, table[class=body] ul, table[class=body] ol, table[class=body] td, table[class=body] span, table[class=body] a { font-size: 16px !important; } table[class=body] .wrapper, table[class=body] .article { padding: 10px !important; } table[class=body] .content { padding: 0 !important; } table[class=body] .container { padding: 0 !important; width: 100% !important; } table[class=body] .main { border-left-width: 0 !important; border-radius: 0 !important; border-right-width: 0 !important; } table[class=body] .btn table { width: 100% !important; } table[class=body] .btn a { width: 100% !important; } table[class=body] .img-responsive { height: auto !important; max-width: 100% !important; width: auto !important; } } /* ------------------------------------- PRESERVE THESE STYLES IN THE HEAD ------------------------------------- */ @media all { .ExternalClass { width: 100%; } .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div { line-height: 100%; } .apple-link a { color: inherit !important; font-family: inherit !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; text-decoration: none !important; } #MessageViewBody a { color: inherit; text-decoration: none; font-size: inherit; font-family: inherit; font-weight: inherit; line-height: inherit; } .btn-primary table td:hover { background-color: #34495e !important; } .btn-primary a:hover { background-color: #34495e !important; border-color: #34495e !important; } } </style></head><body class='' style='background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;'> <table border='0' cellpadding='0' cellspacing='0' class='body' style='border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-color: #f6f6f6;'> <tbody> <tr> <td style='font-family: sans-serif; font-size: 14px; vertical-align: top;'>&nbsp;</td> <td class='container' style='font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; Margin: 0 auto; max-width: 580px; padding: 10px; width: 580px;'> <div class='content' style='box-sizing: border-box; display: block; margin: 2rem; max-width: 580px; padding: 20px; background-color: white;'> <!-- START CENTERED WHITE CONTAINER --> "+data+"<div class='footer' style='clear: both; Margin-top: 10px; text-align: center; width: 100%;'> <table border='0' cellpadding='0' cellspacing='0' style='border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;'> </table> </div> <!-- END FOOTER --> <!-- END CENTERED WHITE CONTAINER --> </div> </td> <td style='font-family: sans-serif; font-size: 14px; vertical-align: top;'>&nbsp;</td> </tr> </tbody> </table></body></html>"
    part2 = MIMEText(html, "html")
    msg.attach(part2)
    s = smtplib.SMTP(email_smtp_server, email_smtp_port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_address, email_password)
    s.sendmail(email_address, reciever, msg.as_string())
    s.quit()
    return f"Email sent to {reciever}"