import uuid

from repositories.event import EventRepository
from models.event import EventModel

event_repository = EventRepository()


async def get_all_events() -> str:
    return await event_repository.get_all()


async def insert_default_event_values():
    if not await get_all_events():
        await event_repository.insert_default_events_values()


async def get_event_by_title(title: str) -> EventModel:
    return await event_repository.get_event_by_title(title)


async def insert_one_event(title: str, event_description: str):
    await event_repository.insert_one(
        {
            "id": uuid.uuid4(),
            "title": title,
            "event_description": event_description
            }
        )
