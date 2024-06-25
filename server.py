import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.smtp import AuthResult, LoginPassword
import email
import signal
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


def authenticator_func(server, session, envelope, mechanism, auth_data):
    # For this simple example, we'll ignore other parameters
    assert isinstance(auth_data, LoginPassword)

    username = auth_data.login.decode()
    password = auth_data.password.decode()

    print(auth_data, password)

    if config.AUTH_DB.get(username) == password:
        print(f"auth {username}: True")
        return AuthResult(success=True, handled=True, auth_data=auth_data)
    else:
        print(f"auth {username}: False")
        return AuthResult(success=False, handled=False)


async def main():
    handler = CustomHandler()
    controller = Controller(
        handler, 
        hostname=config.SMTP_PROXY_HOST, 
        port=config.SMTP_PROXY_PORT,
        authenticator=authenticator_func,
        auth_required=True,
        auth_require_tls=False # disable TLS for the moment
    )
    controller.start()

    print(f"SMTP server running on {config.SMTP_PROXY_HOST}:{config.SMTP_PROXY_PORT}")

    # Create an asyncio Event to wait for shutdown signal
    event = asyncio.Event()

    def handle_sigterm():
        print("\nReceived termination signal, shutting down...")
        event.set()

    # Register signal handlers
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGTERM, handle_sigterm)
    loop.add_signal_handler(signal.SIGINT, handle_sigterm)

    try:
        await event.wait()
    finally:
        controller.stop()
        print("SMTP server stopped")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Something went wrong. {e}")
