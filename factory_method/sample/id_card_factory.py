from factory_method.sample.factory import Factory
from factory_method.sample.id_card import IDCard
from factory_method.sample.product import Product
from typing import List


class IDCardFactory(Factory):
    def __init__(self):
        self._owners: List = []

    def create_product(self, owner: str) -> Product:
        return IDCard(owner=owner)

    # ここjavaだと引数がProduct
    def register_product(self, id_card: IDCard) -> None:
        self._owners.append(id_card.get_owner())

    def get_owners(self) -> List[str]:
        return self._owners
