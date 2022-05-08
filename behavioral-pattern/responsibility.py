

from abc import ABC, abstractmethod
from typing import Optional, Any


class Handler(ABC):

    """
    The Handler interface declares a method for buiding the chain of handlers.
    It also declares a method for excuteing a request
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implement inside a base handler
    class.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convernient way like this:
        # monkey.set_next(squirel).set_next(dog) #
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler is not None:
            return self._next_handler.handle(request)
        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chin
"""


class MonkeyHandler(AbstractHandler):

    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I will eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Requirrel: I will eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I will eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler):
    """
    The client code is usually suited to work a single handler. In most
    cases, it is not even aware that the handler is part if a chain.
    """
    for food in ["Nut", "Banana", "Cup of coffe"]:
        print(f"\nClient: who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"{result}", end="")
        else:
            print(f"{food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    client_code(squirrel)
