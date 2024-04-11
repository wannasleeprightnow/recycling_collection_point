from handlers.events import router as events_router
from handlers.start import router as start_router
from handlers.info import router as info_router
from loader import dp


def include_routers() -> None:
    routers = [
        events_router,
        start_router,
        info_router
        ]
    for router in routers:
        dp.include_router(router)
