from email.message import EmailMessage
import smtplib
import ssl


smtp_server = 'smtp.gmail.com'
port = 587  # For starttls
sender_email = 'sender_email@domain.com'
receiver_email = 'receiver@domain.com'
password = input("Type your password and press enter: ")
message = ' Testing new approaches to use the EmailMessage module'

msg = EmailMessage()
msg.set_content(message)

msg['Subject'] = 'Testing without ehlo'
msg['From'] = sender_email
msg['To'] = receiver_email

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
