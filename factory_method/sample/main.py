from factory_method.sample.id_card_factory import IDCardFactory, Product


def main():
    # factoryをFactory型にするとget_ownersがないという警告が出る。
    factory: IDCardFactory = IDCardFactory()
    card1: Product = factory.create('Aさん')
    card2: Product = factory.create('Bさん')
    card3: Product = factory.create('Cさん')
    card1.use()
    card2.use()
    card3.use()
    owners = factory.get_owners()
    print(owners)


if __name__ == '__main__':
    main()
