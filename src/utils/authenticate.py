from src.errors.auth import UserValidateError
from src.configs.security.security import verify_password
from src.errors.user import UserNotFoundError
from src.di.unit_of_work import AbstractUnitOfWork
from src.models.auth import AuthModel


async def authenticate(
    async_unit_of_work: AbstractUnitOfWork,
    data: AuthModel  
):
    async with async_unit_of_work as auow:
        user: AuthModel = await auow.auth_repo.get_by_email(email=data.email)
        if user is None:
            raise UserNotFoundError()

        if not verify_password(data.password, user.password):
            raise UserValidateError()

    return user