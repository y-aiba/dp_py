from abc import ABCMeta, abstractmethod


class Cloneable(object):
    pass


class Product(Cloneable):
    @abstractmethod
    def use(self) -> None:
        pass

    @abstractmethod
    def create_clone(self) -> object:
        pass
