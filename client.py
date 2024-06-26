import smtplib
from email.message import EmailMessage
import config


username = 'user4'
password = config.AUTH_DB.get(username)

msg = EmailMessage()
msg.set_content("This is a test email")
msg['Subject'] = 'Test Email'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg.add_header('List-Unsubscribe', '<https://list.domain.com/unsubscribe.html?token=123456789>, <mailto:unsubscribe@domain.com?subject=unsubscribe>')

try:
    with smtplib.SMTP(config.SMTP_PROXY_HOST, config.SMTP_PROXY_PORT) as server:
        server.login(username, password)
        server.send_message(msg)
    print("Email sent")
except ConnectionRefusedError:
    print("Unable to connect to SMTP Server. Check if server.py is running")
except smtplib.SMTPNotSupportedError as e:
    print(f"SMTP Error. {e}")
except Exception as e:
    print(f"An exception occurred. {e}")
