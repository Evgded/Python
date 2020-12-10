from abc import abstractmethod, ABC


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat:
    def __init__(self, cost):
        self.cost = cost

    @property
    def consumption(self):
        return self.cost / 6.5 + 0.5


class Suite:
    def __init__(self, cost):
        self.cost = cost

    @property
    def consumption(self):
        return self.cost * 2 + 0.5


my_coat = Coat(48)
my_suite = Suite(182)
print(round(my_coat.consumption + my_suite.consumption, 2))
