from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from models.command import CommandModel


def commands_builder(commands: list[CommandModel]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for command in commands:
        builder.add(
            InlineKeyboardButton(
                text=command.input_text,
                callback_data="cmd_" + str(command.input_text)[:20],
            )
        )
    return builder
