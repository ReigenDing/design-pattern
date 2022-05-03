

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self) -> None:
        self.base_operation1()
        self.base_operation2()
        self.base_operation3()
        self.required_operation1()
        self.required_operation2()
        self.hook1()
        self.hook2()

    def base_operation1(self) -> None:
        pass

    def base_operation2(self) -> None:
        pass

    def base_operation3(self) -> None:
        pass

    @abstractmethod
    def required_operation1(self) -> None:
        pass

    @abstractmethod
    def required_operation2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):

    def base_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented Opetation1")

    def base_operation2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass1 says: Implemented Hook1")

    def required_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented Required Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass1 says: Implemented Required Operation2")

    def hook2(self) -> None:
        print("ConcreteClass1 says: Implemented Hook2")


class ConcreteClass2(AbstractClass):

    def base_operation1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def base_operation2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def required_operation1(self) -> None:
        print("ConcreteClass2 says: Implemented Required Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass2 says: implemented Required Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Implemented Hook1")

    def hook2(self) -> None:
        print("ConcreteClass2 says: Impelemented Hook2")


def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()


if __name__ == "__main__":
    client_code(ConcreteClass1())
    print()
    client_code(ConcreteClass2())
