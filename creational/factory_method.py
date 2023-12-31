"""
Pattern Description :
    In this pattern we hide the creation of object, the client does not know which class is
    getting created. Ideally the client will use some sort of ID (name) and pass it to the factory method ,
    factory method in turn return the concrete object corresponding to this ID (but client has no idea about which class
    has been used to create this object) , only thing client will be aware of the Interface which is followed by the
    product ( i.e. the objects returned by the factory method) .And client will use the product of factory method based
    on this interface
"""

from abc import ABC, abstractmethod
from enum import Enum


class FruitLabel(Enum):
    apple = 'APPLE'
    orange = 'ORANGE'
    kiwi = 'KIWI'


class FruitInterface(ABC):
    @abstractmethod
    def taste(self) -> str:
        pass

    @abstractmethod
    def shape(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @staticmethod
    def price() -> int:
        pass


# create apple class
class Apple(FruitInterface):
    def taste(self) -> str:
        return "Sweet, Tart or a little of both"

    def shape(self) -> str:
        return "Roundish"

    def name(self) -> str:
        return FruitLabel.apple.value

    @staticmethod
    def price() -> int:
        return 10


class Orange(FruitInterface):
    def taste(self) -> str:
        return "Sweet And Tart"

    def shape(self) -> str:
        return "Spherical"

    def name(self) -> str:
        return FruitLabel.orange.value

    @staticmethod
    def price() -> int:
        return 20


class Kiwi(FruitInterface):
    def taste(self) -> str:
        return "Sweet And Sour"

    def shape(self) -> str:
        return "Ovoid"

    def name(self) -> str:
        return FruitLabel.kiwi.value

    @staticmethod
    def price() -> int:
        return 100


class FruitNotAvailableError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return repr(self)


class NotEnoughBalanceError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return repr(self)


class EmptyBasketError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return repr(self)


class Customer:
    def __init__(self, name, wallet_balance):
        self.name = name
        self.wallet_balance = wallet_balance
        self.fruit_basket = list()

    def add_fruit_to_basket(self, fruit: FruitInterface) -> None:
        print(f"{self.name} bought {fruit.name()}")
        self.fruit_basket.append(fruit)

    def get_wallet_balance(self) -> int:
        return self.wallet_balance

    def list_all_fruits_in_basket(self) -> None:
        if len(self.fruit_basket) == 0:
            raise EmptyBasketError(f"{self.name}'s fruit basket is empty !!!")
        print(f"{self.name}'s basket has these fruits:")
        for idx,fruit in enumerate(self.fruit_basket):
            print(f"\t{idx+1}) name = \"{fruit.name()}\", shape = \"{fruit.shape()}\", taste = \"{fruit.taste()}\"")


class FruitStore:
    def __init__(self, name):
        print(f"A fruit store is opened with name {name}")
        self.store_name = name
        self.fruit_store = {}

    def add_fruit_to_store(self, fruit_label: FruitLabel, fruit: FruitInterface) -> None:
        # add single fruit to store
        print(f"{self.store_name} now has {fruit_label.value}'s")
        self.fruit_store[fruit_label] = fruit

    def add_all_fruits_to_store(self):
        # statically add all the fruits in one go
        self.add_fruit_to_store(FruitLabel.apple, Apple)
        self.add_fruit_to_store(FruitLabel.orange, Orange)
        self.add_fruit_to_store(FruitLabel.kiwi, Kiwi)

    def _fruit_is_in_store(self, fruit_id: FruitLabel) -> bool:
        if fruit_id not in self.fruit_store:
            raise FruitNotAvailableError(f"{fruit_id.value} is not available in {self.store_name}")
        return True

    def _customer_has_enough_balance(self, customer: Customer, fruit_id: FruitLabel) -> bool:
        if customer.get_wallet_balance() < self.fruit_store[fruit_id].price():
            raise NotEnoughBalanceError(f"{customer.name} doesn't have the enough balance to buy {fruit_id.value}")
        return True

    def can_buy(self, customer: Customer, fruit_id: FruitLabel) -> bool:
        try:
            self._fruit_is_in_store(fruit_id)
            self._customer_has_enough_balance(customer, fruit_id)
            return True
        except FruitNotAvailableError as e:
            print(e)
            return False
        except NotEnoughBalanceError as e:
            print(e)
            return False
        except Exception as e:
            raise e

    def buy(self, customer: Customer, fruit_id: FruitLabel) -> FruitInterface:
        self._fruit_is_in_store(fruit_id)
        self._customer_has_enough_balance(customer, fruit_id)
        customer.wallet_balance -= self.fruit_store[fruit_id].price()
        return self.fruit_store[fruit_id]()  # instantiation of actual fruit class


fruit_store = FruitStore("PythonFruitFactory")
fruit_store.add_all_fruits_to_store()  # we can even manually add all the fruits to our store through self.add_fruit_to_store method
rohan = Customer("Rohan",110)
if fruit_store.can_buy(rohan,FruitLabel.kiwi):
    fruit = fruit_store.buy(rohan,FruitLabel.kiwi)
    rohan.add_fruit_to_basket(fruit)
if fruit_store.can_buy(rohan,FruitLabel.orange):
    fruit = fruit_store.buy(rohan,FruitLabel.orange)
    rohan.add_fruit_to_basket(fruit)
if fruit_store.can_buy(rohan,FruitLabel.apple):
    fruit = fruit_store.buy(rohan,FruitLabel.apple)
    rohan.add_fruit_to_basket(fruit)
rohan.list_all_fruits_in_basket()


# Output of above code execution
#
# A fruit store is opened with name PythonFruitFactory
# PythonFruitFactory now has APPLE's
# PythonFruitFactory now has ORANGE's
# PythonFruitFactory now has KIWI's
# Rohan bought KIWI
# NotEnoughBalanceError("Rohan doesn't have the enough balance to buy ORANGE")
# Rohan bought APPLE
# Rohan's basket has these fruits:
# 	1) name = "KIWI", shape = "Ovoid", taste = "Sweet And Sour"
# 	2) name = "APPLE", shape = "Roundish", taste = "Sweet, Tart or a little of both"
