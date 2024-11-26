from injector import Injector, singleton, Module, Binder


from .database import AsyncDatabaseAdapter, DatabaseInterface
from .schema import user, UserSchema


class DatabaseModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(DatabaseInterface, to=AsyncDatabaseAdapter())
        binder.bind(UserSchema, to=user)
