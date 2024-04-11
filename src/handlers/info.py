import os

from aiogram import F, Router
from aiogram.types import Message, InputMediaPhoto, FSInputFile

from keyboards.info import info_keyboard
from keyboards.default import default_keyboard
from services.command import get_command_output

router = Router()


@router.message(F.text == "Информация")
async def command_info_handler(message: Message) -> None:
    await message.answer(
        "Какая информация Вас интересует?",
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Назад")
async def command_back_handler(message: Message) -> None:
    await message.answer(
        "Назад!",
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "График работы.")
async def command_how_work_handler(message: Message) -> None:
    await message.answer(
        await get_command_output(message.text),
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Что можно сдать в пункт?")
async def command_what_can_be_handed_handler(message: Message) -> None:
    media_group = []
    for root, _, files in list(os.walk("data/images/can_be_handed")):
        for filename in files:
            media_group.append(
                InputMediaPhoto(media=FSInputFile(
                    os.path.join(root, filename)), caption=filename))
    await message.answer_media_group(
        media=media_group,
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Как правильно сдавать вторсырье?")
async def command_take_it_correctly_handler(message: Message) -> None:
    media_group = []
    for root, _, files in list(os.walk("data/images/take_it_correctly")):
        for filename in files:
            media_group.append(
                InputMediaPhoto(media=FSInputFile(
                    os.path.join(root, filename)), caption=filename))
    await message.answer_media_group(
        media=media_group,
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Есть ли вознаграждение за сданное вторсырье?")
async def command_reward_handler(message: Message) -> None:
    await message.answer(
        await get_command_output(message.text),
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Хотите посотрудничать?")
async def command_collaboration_handler(message: Message) -> None:
    await message.answer(
        await get_command_output(message.text),
        reply_markup=info_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Если не нашлось ответа на мой вопрос?")
async def command_not_answer_handler(message: Message) -> None:
    await message.answer(
        await get_command_output(message.text),
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
