from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from keyboards.default import default_keyboard
from services.command import get_command_output

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        await get_command_output(message.text), reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
