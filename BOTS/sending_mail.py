import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mail_infolar import username, password

server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
server.starttls()

server.login("username", "password")

# server.sendmail("karsanbassalim@gmail.com", "karsanbassergen@gmail.com","What'up")

msg = MIMEMultipart()
msg["From"] = "karsanbassalim@gmail.com"
msg["To"] = "karsanbassergen@gmail.com"
msg["Subject"] = "Robot Uprising"
message = "We are coming for you"
msg.attach(MIMEText(message))

