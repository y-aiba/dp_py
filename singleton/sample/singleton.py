class Singleton(object):
    @classmethod
    def get_instance(cls, input_):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input_)
        else:
            cls._instance.input = input_
        return cls._instance


class MyClass(Singleton):
    def __init__(self, input_):
        self.input = input_


if __name__ == '__main__':
    print("Start.")
    one = MyClass.get_instance(1)
    print(f"one.input={one.input}")
    two = MyClass.get_instance(2)
    print(f"two.input={two.input}")
    one.input = 0
    print(f"one.input={one.input}, two.input={two.input}")
    print(f"one==two: {one==two}")

    # Singletonクラスを単にインスタンス化した場合は異なる
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1==s2: {s1==s2}")

    # MyClassの場合も同じ。上記のようにget_instanceする必要がある。
    m1 = MyClass(1)
    m2 = MyClass(2)
    print(f"m1==m2: {m1==m2}")
