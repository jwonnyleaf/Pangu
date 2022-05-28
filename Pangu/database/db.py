import os
import logging
import dotenv
from typing import Optional



import hikari
from lightbulb import BotApp
import asyncpg

log = logging.getLogger(__name__)

class Database:
    def __init__(self, bot: BotApp) -> None:
        self.bot: BotApp
        self._user = os.environ["PSQL_USER"]
        self._password = os.environ["PSQL_PASSWORD"]
        self._host = os.environ["PSQL_HOST"]
        self._port = int(os.environ["PSQL_PORT"])
        self._db_id = os.environ["PSQL_DB_ID"]
        self._pool = asyncpg.Pool
        self._connected = False


    async def connect(self) -> None:
        if self._connected:
            raise Exception("Database is already Connected.")

        self._pool = await asyncpg.create_pool(f"postgres://postgres:UXahjK5GLRx9ziyw@winhost:5432/postgres")
        self._connected = True
        log.info("** Database is Connected.")

    async def execute(self, query: str, *args, timeout: Optional[float] = None) -> str:
        if not self._pool:
            raise Exception("Database is not Connected")

        return await self._pool.execute(query, *args, timeout = timeout)

    async def close(self) -> None:
        if not self._connected:
            raise Exception("Database is not Connected.")

        await self._pool.close()
        self._connected = False
        log.info("** Database is Closed.")


