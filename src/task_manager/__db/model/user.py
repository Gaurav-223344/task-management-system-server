# import asyncpg
from typing import List, Optional

from injector import inject, singleton

from src.task_manager.utils.decorators import StandardSingletonDecorator

from ..database import DatabaseInterface
from ..types import UserSchema

@StandardSingletonDecorator
class UserModel:
    @inject
    def __init__(self, schema: UserSchema, adaptor: DatabaseInterface):
        self.schema = schema
        self.adaptor = adaptor

    async def create_table(self):
        try:
            query = f"""
                CREATE TABLE IF NOT EXISTS users (
                    {self.schema}
                );
            """
            await self.execute(query)
            return True
        except Exception as e:
            print('An exception occurred')
            print(e)
            return False

    async def fetch_all(self, query: str, *args):
        return await self.adaptor.fetch_data(query, *args)

    async def fetch_one(self, query: str, *args):
        return await self.adaptor.fetch_one(query, *args)

    async def execute(self, query: str, *args):
        return await self.adaptor.execute_query(query, *args)
