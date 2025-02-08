from fastapi_mail import ConnectionConfig, MessageSchema, MessageType

from src.configs.settings.settings import settings

connection_config = ConnectionConfig(
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_USERNAME=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


def get_message_schema(email: str, token: str) -> MessageSchema:
    return MessageSchema(
        subject = "Подтверждение аккаунта",
        recipients = [email],
        body = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Подтверждение аккаунта</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                        text-align: center;
                    }}
                    .container {{
                        max-width: 500px;
                        background: white;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                        margin: 20px auto;
                    }}
                    .button {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: white;
                        background-color: #007bff;
                        text-decoration: none;
                        border-radius: 5px;
                        margin-top: 20px;
                    }}
                    .button:hover {{
                        background-color: #0056b3;
                    }}
                    .footer {{
                        margin-top: 20px;
                        font-size: 12px;
                        color: #777;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Подтверждение аккаунта</h2>
                    <p>Здравствуйте! Благодарим вас за регистрацию.</p>
                    <p>Чтобы подтвердить ваш аккаунт, нажмите на кнопку ниже:</p>
                    <a class="button" href="http://localhost:8000/api/v1/auth/verify/email?email={email}&verify_token={token}">
                        Подтвердить аккаунт
                    </a>
                    <p class="footer">Если вы не регистрировались на нашем сайте, просто проигнорируйте это письмо.</p>
                </div>
            </body>
            </html>
        """,
        subtype = MessageType.html
    )