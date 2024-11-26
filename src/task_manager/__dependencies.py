from injector import Injector, singleton, Module, Binder

from .__db.dependencies import DatabaseModule


from .__db.database import AsyncDatabaseAdapter, DatabaseInterface
from .__db.schema import user, UserSchema


class TaskManagerModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.install(DatabaseModule) 
