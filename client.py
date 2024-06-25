import smtplib
from email.message import EmailMessage
import config


msg = EmailMessage()
msg.set_content("This is a test email")
msg['Subject'] = 'Test Email'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'

with smtplib.SMTP(config.SMTP_PROXY_HOST, config.SMTP_PROXY_PORT) as server:
    server.send_message(msg)

print("Email sent")
