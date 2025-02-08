from fastapi_mail import FastMail
from src.configs.mail.config import connection_config

fast_mail = FastMail(connection_config)
