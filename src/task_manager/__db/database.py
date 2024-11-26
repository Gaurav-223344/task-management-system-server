from abc import ABC, abstractmethod
from typing import List, Optional
import asyncpg
from injector import singleton

from ..utils.decorators import StandardSingletonDecorator


class DatabaseInterface(ABC):
    @abstractmethod
    async def connect(self, host: str, port: int, user: str, password: str, database: str):
        pass

    @abstractmethod
    async def execute_query(self, query: str, *args):
        pass

    @abstractmethod
    async def fetch_data(self, query: str, *args):
        pass

    @abstractmethod
    async def close(self):
        pass


@StandardSingletonDecorator
class AsyncDatabaseAdapter(DatabaseInterface):
    def __init__(self):
        self.pool = None  # Connection pool will be initialized later

    async def connect(self, host: str, port: int, user: str, password: str, database: str):
        # Create a connection pool
        self.pool: asyncpg.Pool = await asyncpg.create_pool(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            min_size=10,  # Minimum pool size
            max_size=20,  # Maximum pool size
        )
        print("Connected to the database with a connection pool.")

    async def execute_query(self, query: str, *args):
        try:
            async with self.pool.acquire() as connection:
                result = await connection.execute(query, *args)
                return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    async def fetch_data(self, query: str, *args) -> List[asyncpg.Record]:
        try:
            async with self.pool.acquire() as connection:
                result = await connection.fetch(query, *args)
                return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    async def fetch_one(self, query: str, *args) -> Optional[asyncpg.Record]:
        try:
            async with self.pool.acquire() as connection:
                result = await connection.fetchrow(query, *args)
                return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    async def close(self):
        if self.pool:
            await self.pool.close()
            print("Connection pool closed.")
