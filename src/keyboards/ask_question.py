from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

ask_question_keyboard = (
    ReplyKeyboardBuilder()
    .row(
        KeyboardButton(text="Задать вопрос ИИ"),
        KeyboardButton(text="По номеру телефона/в группе Вконтакте")
    )
    .row(
        KeyboardButton(text="Сотрудничество"),
        KeyboardButton(text="Назад"),
    ).adjust(2)
)
