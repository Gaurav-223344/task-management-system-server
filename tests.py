from injector import Injector, singleton, inject, Module, Binder
from abc import ABC, abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def run(self):
        pass


@singleton
class MySingletonClass(MyInterface):
    def __init__(self):
        self.data = None  # Call run method during initialization

    def run(self):
        self.data = 1

class secondClass:
    @inject
    def __init__(self, service:MyInterface):
        self.service = service


class TestModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(MyInterface, to=MySingletonClass(), scope=singleton)

# Usage
injector = Injector([TestModule])

instance1 = injector.get(MyInterface)
instance1.run()
instance2 = injector.get(MyInterface)
print(instance2.data)
instance3 = injector.get(secondClass)
print(instance3.service.data)

