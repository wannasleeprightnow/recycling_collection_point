from exceptions import UserNotExists
from models.user import UserModel
from repositories.user import UserRepository

user_repository = UserRepository()


async def insert_one_user(telegram_username: str) -> UserModel:
    return await user_repository.insert_one(
        {"telegram_username": telegram_username}
        )


async def is_user_admin(telegram_username: str) -> bool:
    if (user := await user_repository.get_one_user(telegram_username)) is None:
        return False
    return user.is_admin


async def set_user_admin(telegram_username: str) -> None:
    if await user_repository.get_one_user(telegram_username):
        await user_repository.set_user_admin(telegram_username)
    else:
        raise UserNotExists


async def get_user_by_username(telegram_username: str) -> bool:
    return (await user_repository.get_one_user(telegram_username)) is not None
