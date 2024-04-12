from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

info_keyboard = (
    ReplyKeyboardBuilder()
    .row(
        KeyboardButton(text="График работы."),
        KeyboardButton(text="Какие мероприятия проводит «Птичка»?"))
    .row(
        KeyboardButton(text="Что можно сдать в пункт?"),
        KeyboardButton(text="Как правильно сдавать вторсырье?"))
    .row(
        KeyboardButton(text="Есть ли вознаграждение за сданное вторсырье?"),
        KeyboardButton(text="Назад")
        )
    ).adjust(2)
