from abc import ABCMeta, abstractmethod
from factory_method.sample.product import Product


class Factory(metaclass=ABCMeta):
    def create(self, owner: str) -> Product:
        p: Product = self.create_product(owner=owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner: str) -> Product:
        pass

    @abstractmethod
    def register_product(self, p: Product) -> None:
        pass
