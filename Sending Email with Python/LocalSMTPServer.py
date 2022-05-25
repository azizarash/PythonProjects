# import modules and packages
import smtplib
from email.message import EmailMessage

# define email attributes
subject = "Test Email Subject"
sender = "sender@example.com"
receiver = "receiver@example.com"

# define email object
msg = EmailMessage()

# set headers
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

# set body text
msg.set_content("This is test email body on local server...")

# define port
port = 1025

# call smtplib.SMTP in the with context manager
with smtplib.SMTP('localhost', port) as server:
    # send message
    server.send_message(msg)
    # print result to run console
    print("Test email sent successfully!")