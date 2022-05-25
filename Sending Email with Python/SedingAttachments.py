# Sending Attachments with Email
# import modules and classes
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# server and port
smtp_server = "smtp.mailtrap.io"
port = 2525

# your login credentials generated by Mailtrap
login = "<your user_id>"
password = "<your password>"

# sender and receiver emails
sender = "sender@example.com"
receiver = "receiver@example.com"

# message object
message = MIMEMultipart()
message["Subject"] = "PyCharm Keymap Reference"
message["From"] = sender
message["To"] = receiver

# email body
email_body = "You may find the Keymap Reference of PyCharm IDE in the attachments."
message.attach(MIMEText(email_body, "plain"))

# file info
filepath = "files/ReferenceCardForMac.pdf"
filename = "ReferenceCardForMac.pdf"

# open the PDF file in read-binary mode
with open(filepath, "rb") as attachment:
    # content type "application/octet-stream" means
    # a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encoding => to base64
encoders.encode_base64(part)

# Add mail header
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to the message and convert it to string
message.attach(part)
text = message.as_string()

# send the email with attachment
with smtplib.SMTP(smtp_server, port) as server:
    try:
        server.login(login, password)
        server.sendmail(sender, receiver, text)
    except Exception as ex:
        print(ex)
    else:
        print("Mail with attachment sent successfully...")
