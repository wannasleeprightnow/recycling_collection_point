from dataclasses import dataclass
from os import environ
from typing import Literal

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    MODE: Literal["PROD", "DEV", "TEST"] = "DEV"

    TOKEN_DEV_TEST_BOT: str = "6889866525:AAF2T2ik2grBYZvuyRT06REwCeIoA_N9wlM"
    TOKEN_PROD_BOT: str = environ.get("TOKEN_PROD_BOT")

    POSTGRES_USER: str = environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST")
    POSTGRES_PORT: str = environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = environ.get("POSTGRES_DB")
    POSTGRES_DSN: str = f"postgresql+asyncpg://{POSTGRES_USER}:\
{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLITE_DSN: str = "sqlite+aiosqlite:///db.sqlite3"
