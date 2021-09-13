from factory_method.sample.product import Product


class IDCard(Product):
    def __init__(self, owner: str):
        print(f"{owner}のカードを作ります")
        self.owner = owner

    def use(self) -> None:
        print(f"{self.owner}のカードを使います")

    def get_owner(self) -> str:
        return self.owner
