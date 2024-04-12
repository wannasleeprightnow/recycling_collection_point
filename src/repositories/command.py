from uuid import UUID

from sqlalchemy import insert, select, update

from default_values import default_commands_values
from db.database import async_session_maker
from models.command import CommandModel
from repositories.repository import Repository


class CommandRepository(Repository):
    model = CommandModel

    async def get_command(self, input_text: str) -> CommandModel:
        async with async_session_maker() as session:
            query = (select(self.model.output_text)
                     .where(self.model.input_text == input_text)
                     )
            result = await session.execute(query)
            return result.scalars().one_or_none()

    async def get_command_by_start_input(self, input_text: str) -> CommandModel:
        async with async_session_maker() as session:
            query = (select(self.model)
                     .where(self.model.input_text.startswith(input_text))
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

    async def update_command_output(
        self, new_output: str, command_id: UUID
    ) -> None:
        async with async_session_maker() as session:
            stmt = (update(self.model)
                    .where(self.model.id == command_id)
                    .values({"output_text": new_output})
            )
            await session.execute(stmt)
            await session.commit()
