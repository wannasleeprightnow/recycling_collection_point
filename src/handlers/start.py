from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from keyboards.default import default_keyboard
from services.command import get_command
from services.user import get_user_by_username, insert_one_user

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if not (await get_user_by_username(message.from_user.username)):
        await insert_one_user(message.from_user.username)
    await message.answer(
        await get_command(message.text),
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
