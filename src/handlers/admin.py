from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode

from exceptions import UserNotExists
from keyboards.admin import admin_keyboard
from keyboards.command import commands_builder
from keyboards.default import default_keyboard
from services.command import get_all_commands, get_command_by_start_input, update_command_output
from services.user import is_user_admin, set_user_admin

router = Router()


class AdminUsername(StatesGroup):
    username = State()


class NewOutputText(StatesGroup):
    command_id = State()
    new_output = State()


@router.message(Command("admin"))
async def command_admin_mode_handler(message: Message) -> None:
    if await is_user_admin(message.from_user.username):
        await message.answer(
            "Вы перешли в режим адмистратора!",
            reply_markup=admin_keyboard.as_markup(resize_keyboard=True)
            )
    else:
        await message.answer(
            "У вас отсутствуют права администратора.",
            reply_markup=default_keyboard.as_markup(resize_keyboard=True)
            )


@router.message(F.text == "Назначить администратора")
async def command_set_new_admin_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Введите его имя пользователя в Телеграм",
        reply_markup=admin_keyboard.as_markup(resize_keyboard=True)
        )
    await state.set_state(AdminUsername.username)


@router.message(F.text == "Выйти")
async def command_leave_admin_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Вы вышли из режима администратора.",
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(AdminUsername.username)
async def set_admin(message: Message, state: FSMContext):
    try:
        if await is_user_admin(message.from_user.username):
            await set_user_admin(message.text)
            await message.answer(
                f"Пользователь @{message.text} получил права администратора.",
                reply_markup=admin_keyboard.as_markup(resize_keyboard=True))
        else:
            await message.answer(
                "У вас отсутствуют права администратора.",
                reply_markup=default_keyboard.as_markup(resize_keyboard=True)
            )
    except UserNotExists:
        await message.answer(
            "Такого пользователя не существует!",
            reply_markup=admin_keyboard.as_markup(resize_keyboard=True))
    await state.clear()


@router.message(F.text == "Отредактировать вывод команд")
async def command_choose_command_handler(message: Message, state: FSMContext) -> None:
    commands = await get_all_commands()
    await message.answer(
        "Выберите необходимую команду",
        reply_markup=commands_builder(commands).adjust(1).as_markup(resize_keyboard=True)
        )


@router.callback_query(F.data.startswith("cmd_"))
async def command_callback(callback: CallbackQuery, state: FSMContext):
    command = await get_command_by_start_input(callback.data[4:])
    await callback.message.answer(
        f'Введите новый вывод для команды "{command.input_text}"',
        reply_markup=admin_keyboard.as_markup(resize_keyboard=True),
        parse_mode=ParseMode.HTML
    )
    await callback.message.delete()
    await state.update_data(command_id=command.id)
    await state.set_state(NewOutputText.new_output)


@router.message(NewOutputText.new_output)
async def set_new_output_text(message: Message, state: FSMContext):
    await state.update_data(new_output=message.text)
    if await is_user_admin(message.from_user.username):
        data = await state.get_data()
        await state.clear()
        await update_command_output(**data)
        await message.answer("Команда успешно отредактирована.")
    else:
        await message.answer(
            "У вас отсутствуют права администратора.",
            reply_markup=default_keyboard.as_markup(resize_keyboard=True)
            )
