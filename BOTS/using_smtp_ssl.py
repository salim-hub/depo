import smtplib, ssl
from mail_infolar import password

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("salimkarsanbas@gmail.com", password)


#   python -m smtpd -c DebuggingServer -n localhost:1025