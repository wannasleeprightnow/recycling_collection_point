from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from settings import Settings

dp = Dispatcher()

match Settings.MODE:
    case "PROD":
        bot = Bot(Settings.TOKEN_PROD_BOT, parse_mode=ParseMode.HTML)
    case _:
        bot = Bot(Settings.TOKEN_DEV_TEST_BOT, parse_mode=ParseMode.HTML)
