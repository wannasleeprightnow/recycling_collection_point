from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from models.event import EventModel


def events_builder(events: list[EventModel]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for event in events:
        builder.add(
            InlineKeyboardButton(
                text=event.title,
                callback_data="event_" + str(event.id),
            )
        )
    return builder
