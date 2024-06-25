import asyncio
from aiosmtpd.controller import Controller
import email
import config


class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        data = envelope.content

        message = email.message_from_bytes(data)

        # log the email details
        print(f"Mail from: {mail_from}")
        print(f"Recipients: {rcpt_tos}")
        print(f"Message subject: {message['subject']}")
        
        # store email in database

        return '250 OK'


async def main():
    handler = CustomHandler()
    controller = Controller(handler, hostname=config.SMTP_PROXY_HOST, port=config.SMTP_PROXY_PORT)
    controller.start()

    print('SMTP server running on localhost:1025')

    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()


if __name__ == '__main__':
    asyncio.run(main())
