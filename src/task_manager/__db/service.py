import asyncio

from injector import Injector, singleton


from .database import DatabaseInterface
from .model.user import UserModel
from .dependencies import DatabaseModule
from .config import POSTGRES_DATABASE, POSTGRES_HOST, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER


async def connect():
    try:
        db_injector = Injector([DatabaseModule])
        database_service = db_injector.get(DatabaseInterface)

        await database_service.connect(
            POSTGRES_HOST,
            POSTGRES_PORT,
            POSTGRES_USER,
            POSTGRES_PASSWORD,
            POSTGRES_DATABASE
        )
        print("connected successfully to the database")
    except Exception as e:
        print('Something went wrong while connecting to the database')
        print(e)


async def create_table(model, table_name: str):
    create_user_table = await model.create_table()
    if create_user_table:
        print(f"{table_name} table created successfully")
    else:
        print(f"Error while creating {table_name} table")


async def create_tables():
    injector = Injector([DatabaseModule])
    await create_table(injector.get(UserModel), "User")


async def database_setup():
    await connect()
    await create_tables()
