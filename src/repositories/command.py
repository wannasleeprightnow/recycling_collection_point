from sqlalchemy import insert, select

from default_values import default_commands_values
from db.database import async_session_maker
from models.command import CommandModel
from repositories.repository import Repository


class CommandRepository(Repository):
    model = CommandModel

    async def get_command_output(self, input_text: str) -> CommandModel:
        async with async_session_maker() as session:
            query = (select(self.model.output_text)
                     .where(self.model.input_text == input_text)
                     )
            result = await session.execute(query)
            return result.scalars().one_or_none()

    async def insert_default_command_values(
        self
    ) -> None:
        async with async_session_maker() as session:
            for i in default_commands_values:
                stmt = insert(self.model).values(**i)
                await session.execute(stmt)
            await session.commit()
