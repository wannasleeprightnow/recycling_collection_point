from sqlalchemy import insert, select

from models.event import EventModel
from db.database import async_session_maker
from repositories.repository import Repository
from default_values import default_events_values


class EventRepository(Repository):
    model = EventModel

    async def insert_default_events_values(
        self
    ) -> None:
        async with async_session_maker() as session:
            for i in default_events_values:
                stmt = insert(self.model).values(**i)
                await session.execute(stmt)
            await session.commit()

    async def get_event_by_title(self, title: str) -> EventModel:
        async with async_session_maker() as session:
            query = select(EventModel).where(EventModel.title == title)
            result = await session.execute(query)
            return result.scalar_one()
