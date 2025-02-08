from src.configs.mail import fast_mail
from src.configs.mail.config import get_message_schema


async def send_verification_mail(email: str, verification_token: str):
    await fast_mail.send_message(get_message_schema(email=email, token=verification_token))