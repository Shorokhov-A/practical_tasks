from abc import ABC, abstractmethod


class ClothesAbs(ABC):
    @abstractmethod
    def __init__(self, name):
        self._name = str(name)

    @abstractmethod
    def cloth_consumption(self):
        pass


class CoatAbs(ABC):
    @abstractmethod
    def __init__(self, size):
        self._size = float(size)

    @abstractmethod
    def cloth_consumption(self):
        pass


class SuitAbs(ABC):
    @abstractmethod
    def __init__(self, height):
        self._height = float(height)

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(CoatAbs):
    def __init__(self, size):
        super().__init__(size)

    @property
    def cloth_consumption(self):
        result = self._size / 6.5 + 0.5
        return result


class Suit(SuitAbs):
    def __init__(self, height):
        super().__init__(height)

    @property
    def cloth_consumption(self):
        result = self._height * 2 + 0.3
        return result


class Clothes(ClothesAbs):
    def __init__(self, name):
        super().__init__(name)
        self.clothes = []

    def cloth_consumption(self):
        result = 0
        for el in self.clothes:
            result += el.cloth_consumption
        print(f'Суммарный расход ткани на производство одежды '
              f'«{self._name}»:\n{round(result, 2)}')
        return result

    def add_coat(self, size):
        self.clothes.append(Coat(size))
        print(f'Пальто:\nразмер: {size},\n'
              f'расход ткани: {Coat(size).cloth_consumption}')

    def add_suit(self, height):
        self.clothes.append(Suit(height))
        print(f'Костюм:\nрост: {height},\n'
              f'расход ткани: {Suit(height).cloth_consumption}')


if __name__ == '__main__':
    products = Clothes('Большевичка')
    products.add_coat(56)
    products.add_coat(58)
    products.add_suit(190)
    products.add_suit(175)
    print(products.cloth_consumption())
