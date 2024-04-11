from aiogram import F
from aiogram.types import CallbackQuery, Message
from aiogram import Router

from keyboards.events import events_builder
from keyboards.default import default_keyboard
from keyboards.info import info_keyboard
from services.event import get_all_events, get_event_by_id

router = Router()


@router.message(F.text == "Какие мероприятия проводит «Птичка»?")
async def command_events_list_handler(message: Message) -> None:
    events = await get_all_events()
    await message.answer(
        "Мероприятия",
        reply_markup=events_builder(events).adjust(1).as_markup(resize_keyboard=True)
        )


@router.callback_query(F.data.startswith("event_"))
async def divided_books_callback(callback: CallbackQuery):
    event = await get_event_by_id(callback.data[6:])
    await callback.message.answer(
        event.event_description,
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
    )


@router.message(F.text == "Назад")
async def command_back_handler(message: Message) -> None:
    await message.answer(
        "Назад!",
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
