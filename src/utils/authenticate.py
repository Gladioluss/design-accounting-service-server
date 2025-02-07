from src.errors.auth import IncorrectLoginError
from src.configs.security.security import verify_password
from src.di.unit_of_work import AbstractUnitOfWork
from src.models.auth import AuthModel


async def authenticate(
    async_unit_of_work: AbstractUnitOfWork,
    data: AuthModel  
):
    async with async_unit_of_work as auow:
        user: AuthModel = await auow.auth_repo.get_by_email(email=data.email)
        if user is None:
            raise IncorrectLoginError()

        if not verify_password(data.password, user.password):
            raise IncorrectLoginError()

    return user