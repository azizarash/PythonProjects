# send email to Mailtrap fake server

import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Messege Content
"""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    try:
        server.login("<your user_id>", "<your password>")
        server.sendmail(sender, receiver, message)
    except Exception as ex:
        print(ex)
    else:
        print("Message sent successfully to Mailtrap.")

