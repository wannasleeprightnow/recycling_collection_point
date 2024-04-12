from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin_keyboard = (
    ReplyKeyboardBuilder()
    .row(
        KeyboardButton(text="Назначить администратора"),
        KeyboardButton(text="Отредактировать вывод команд")
    )
    .row(
        KeyboardButton(text="Выйти")
    ).adjust(1)
)
