import asyncio
import logging
import sys

from loader import bot, dp
from handlers.routers import include_routers
from services.command import (
    insert_default_command_values
)
from services.event import (
    insert_default_event_values
)
from db.database import create_db


async def main():
    await create_db()
    await insert_default_command_values()
    await insert_default_event_values()
    include_routers()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
