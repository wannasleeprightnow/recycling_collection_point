from handlers.admin import router as admin_router
from handlers.ask_question import router as ask_question_router
from handlers.events import router as events_router
from handlers.start import router as start_router
from handlers.info import router as info_router
from loader import dp


def include_routers() -> None:
    routers = [
        admin_router,
        ask_question_router,
        events_router,
        start_router,
        info_router
        ]
    for router in routers:
        dp.include_router(router)
