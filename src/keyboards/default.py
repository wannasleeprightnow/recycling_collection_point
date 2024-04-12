from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

default_keyboard = (
    ReplyKeyboardBuilder()
    .row(
        KeyboardButton(text="Информация"),
        KeyboardButton(text="Задать вопрос")
    )
    .row(
        KeyboardButton(text="Помощь"),
    ).adjust(2)
)
