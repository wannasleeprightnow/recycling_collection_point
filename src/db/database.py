from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from settings import Settings


class Base(DeclarativeBase):

    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}"
                for col in self.__table__.columns.keys()]
        return " ".join(cols)


async_engine = create_async_engine(Settings.POSTGRES_DSN, echo=False)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_db():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
