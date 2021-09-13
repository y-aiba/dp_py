from factory_method.sample.id_card_factory import Factory, IDCardFactory, Product


class Main:
    @staticmethod
    def main():
        factory: Factory = IDCardFactory()
        card1: Product = factory.create('Aさん')
        card2: Product = factory.create('Bさん')
        card3: Product = factory.create('Cさん')
        card1.use()
        card2.use()
        card3.use()


if __name__ == '__main__':
    m = Main()
    m.main()
