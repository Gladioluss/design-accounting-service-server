from app.configs.security.security import verify_password
from src.errors.auth import UserAlreadyExists
from src.configs.security.security import encrypt_password
from src.models.auth import AuthModel
from src.di.unit_of_work import AbstractUnitOfWork
from src.utils.authenticate import authenticate


async def signup(
   async_unit_of_work: AbstractUnitOfWork, 
   data: AuthModel     
) -> None:
    async with async_unit_of_work as auow:
        user = await auow.auth_repo.get_by_email(email=data.email)

        if user is not None:
            raise UserAlreadyExists(data.email)
        data.password = encrypt_password(password=data.password)
        await auow.auth_repo.create(data=data)

async def signin(
    async_unit_of_work: AbstractUnitOfWork, 
    data: AuthModel     
):
    user = await authenticate(async_unit_of_work=async_unit_of_work, data=data)
