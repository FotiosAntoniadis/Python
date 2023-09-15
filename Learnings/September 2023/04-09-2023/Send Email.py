import smtplib

sender = "#################@gmail.com"
receiver = "#################@gmail.com"
password = "#########"
subject = "Python Email Test"
body = "This is a Email created and sent by a Python Program"


# Header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been Sent.")
except smtplib.SMTPAuthenticationError:
    print("Unable to Sign In")


# 04/09/23