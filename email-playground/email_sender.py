from email.message import EmailMessage
import smtplib
import ssl
from pathlib import Path
from string import Template
# from email.mime.text import MIMEText


smtp_server = 'smtp.gmail.com'
port = 587  # For starttls
sender_email = 'mymail@gmail.com'
receiver_name = 'james'
receiver_email = ['your2@gmail.com', 'your3@yahoo.com']
password = input("Type your password and press enter: ")
# message = ' Testing new approaches to use the EmailMessage module'

html = Template(Path('index.html').read_text())
msg = EmailMessage()
msg['Subject'] = 'First html email'
msg['From'] = sender_email
msg['To'] = receiver_email

msg.set_content(html.substitute(
    {'name': 'Your_name', 'r_name': receiver_name}), 'html')


# Create a secure SSL context
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context)
    server.login(sender_email, password)
    server.send_message(msg)
except Exception as e:
    print(e)
finally:
    server.quit()
