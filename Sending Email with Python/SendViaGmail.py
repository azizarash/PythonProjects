# Sending Emails via Gmail
# import libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# server and port
smtp_server = "smtp.gmail.com"
port = 587  # for STARTTLS connection

content = '''
Email Content

'''

# mail addresses and password
sender = '<your_gmail_address>@gmail.com'
password = '<your_gmail_password>'
receiver = 'receiver@example.com'

# set MIME data
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Email sent from Python to Gmail.'

# set the body
message.attach(MIMEText(content, 'plain'))

# create SMTP session
session = smtplib.SMTP('smtp.gmail.com', port)

# enable security
session.starttls()

# login with credentials
session.login(sender, password)

# convert message to string before sending
text = message.as_string()

# send the email
session.sendmail(sender, receiver, text)

# close the session
session.quit()
