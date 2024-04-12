from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
import g4f

from keyboards.ask_question import ask_question_keyboard

from keyboards.default import default_keyboard
from services.command import get_command

router = Router()


class Question(StatesGroup):
    question = State()


@router.message(F.text == "Задать вопрос")
async def command_ask_question_handler(message: Message) -> None:
    await message.answer(
        "Как вы хотите задать вопрос?",
        reply_markup=ask_question_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Задать вопрос ИИ")
async def command_ask_question_ai_handler(
    message: Message, state: FSMContext
) -> None:
    await message.answer(
        "Введите Ваш вопрос",
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
    await state.set_state(Question.question)


@router.message(Question.question)
async def deskmate_chosen(message: Message, state: FSMContext):
    response = ''.join(await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.FlowGpt,
        messages=[{"role": "user", "content": message.text}]
    ))
    await message.answer(
        response,
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
    await state.clear()


@router.message(F.text == "По номеру телефона/в группе Вконтакте")
async def command_not_answer_handler(message: Message) -> None:
    await message.answer(
        await get_command(message.text),
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )


@router.message(F.text == "Сотрудничество")
async def command_collaboration_handler(message: Message) -> None:
    await message.answer(
        await get_command(message.text),
        reply_markup=default_keyboard.as_markup(resize_keyboard=True)
        )
