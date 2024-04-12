from models.user import UserModel
from repositories.repository import Repository

from sqlalchemy import select, update

from db.database import async_session_maker
from repositories.repository import Repository


class UserRepository(Repository):
    model = UserModel

    async def get_one_user(self, username: str) -> UserModel:
        async with async_session_maker() as session:
            query = select(UserModel).where(
                UserModel.telegram_username == username
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def set_user_admin(self, username: str):
        async with async_session_maker() as session:
            stmt = (update(UserModel)
                    .where(UserModel.telegram_username == username)
                    .values({"is_admin": True}))
            await session.execute(stmt)
            await session.commit()
