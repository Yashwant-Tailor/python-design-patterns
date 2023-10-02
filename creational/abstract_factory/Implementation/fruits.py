from creational.abstract_factory.interfaces import Fruit, ProductFactory
from enum import Enum
from typing import Optional, Any


class FruitLabel(Enum):
    apple = "Apple"
    watermelon = "WaterMelon"
    orange = "Orange"
    random_fruit = "random_fruit"


class FruitFactory(ProductFactory):
    """
    NOTE : In this factory we will register all the fruit products templates
    """

    def add_one_item(self, fruit_label: FruitLabel, fruit: Fruit) -> None:
        """
        add one fruit label and fruit to our factory
        :param fruit_label:
        :param fruit:
        :return:
        """
        self.factory[fruit_label] = fruit

    def add_all_item(self) -> None:
        """
        For now the implementation is static (we have hardcoded all the fruit template needs to be added , but it can
        be dynamic where we will pass all the fruit template needs to be added in this factory)
        :return:
        """
        print("Adding all the fruits")
        all_fruits = [(FruitLabel.apple, Apple), (FruitLabel.watermelon,
                                                  WaterMelon)]  # Note that we only registered the class template not the instance of the class
        for fruit_label, fruit in all_fruits:
            self.add_one_item(fruit_label, fruit)

    def is_item_available(self, fruit_label: Any) -> bool:
        """
        check that the fruit available to this corresponding fruit label
        :param fruit_label:
        :return: True/False
        """
        return fruit_label in self.factory

    def get_item(self, fruit_label: FruitLabel) -> Optional:
        """
        Get the actual instance of the fruit if fruit_label is present in our factory otherwise return None
        :param fruit_label:
        :return:
        """
        if fruit_label in self.factory:
            return self.factory[fruit_label]()
        return None

    def get_item_template(self, fruit_label: FruitLabel) -> Optional:
        """
        Get the template of the fruit if fruit_label is present in our factory otherwise return None
        :param fruit_label:
        :return:
        """
        if fruit_label in self.factory:
            return self.factory[fruit_label]
        return None


class Apple(Fruit):
    def name(self) -> str:
        return "Apple"

    def category(self) -> str:
        return Fruit.category() + " -> Apple"

    @staticmethod
    def price() -> float:
        return 10.0

    def shape(self) -> str:
        return "Roundish"

    def taste(self) -> str:
        return "Sweet & Tart"

    def vitamins_in_fruit(self) -> list[str]:
        return ["riboflavin", "thiamin", "B6"]

    def is_high_fiber(self) -> bool:
        return True


class WaterMelon(Fruit):
    def name(self) -> str:
        return "WaterMelon"

    def category(self) -> str:
        return Fruit.category() + " -> WaterMelon"

    @staticmethod
    def price() -> float:
        return 5.45

    def shape(self) -> str:
        return "Oval"

    def taste(self) -> str:
        return "Sweet & fruity"

    def vitamins_in_fruit(self) -> list[str]:
        return ["A", "B6", "C"]

    def is_high_fiber(self) -> bool:
        return False
