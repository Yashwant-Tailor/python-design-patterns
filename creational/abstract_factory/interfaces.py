"""
Pattern Description:
    In this pattern , we group the factories ( ideally one factory generates different products
    of an interface, but if you have more than one interface then creating all the products through one factory might not
    be manageable, that's why we use the abstract factory to kind of group all the factories for each interface ,
    and let them have their own implementations)
    In this pattern client only need to be aware of methods of interface (not the concreate classes of these interface)
    and using this knowledge client will take appropriate action with a particular product (concrete class of the interface)
"""
from abc import ABC, abstractmethod
from typing import Any, Optional


class ShopProduct(ABC):
    """
    Interface , followed by every product in the shop
    This interface will have basic feature of a product
    """

    @abstractmethod
    def name(self) -> str:
        """
        :return: name of the product
        """
        pass

    @abstractmethod
    def category(self) -> str:
        """
        :return: category of the product
        NOTE : final category will be combination of all the parent + actual category of the product
        Example : if parent category is "par_cat1" and actual product catgegory is "prod_cat"
                    ,then final category will be "par_cat1 -> prod_cat"
        """
        pass

    @staticmethod
    def price() -> float:
        """
        :return: price of the product
        """
        pass

    @abstractmethod
    def shape(self) -> str:
        """
        :return: shape of the product
        """
        pass


class Fruit(ShopProduct,ABC):
    """
    All fruits should implement this interface
    """

    @staticmethod
    def category() -> str:
        """
        Static method to return the category of all fruits implementing this interface
        :return:
        For more details refer : category method of ShopProduct
        """
        return "Fruit"

    @abstractmethod
    def taste(self) -> str:
        """
        :return: taste of the fruit
        """
        pass

    @abstractmethod
    def vitamins_in_fruit(self) -> list[str]:
        """
        :return: list of vitamins available in the fruit
        """
        pass

    @abstractmethod
    def is_high_fiber(self) -> bool:
        """
        :return: True/False
        """
        pass


class SmartPhone(ShopProduct,ABC):
    """
    All SmartPhone should implement this method
    """

    @staticmethod
    def category() -> str:
        """
        Static method to return the category of all smartphones implementing this interface
        :return:
        For more details refer : category method of ShopProduct
        """
        return "SmartPhone"

    @abstractmethod
    def battery(self) -> str:
        """
        :return: battery of the smartphone
        """
        pass

    @abstractmethod
    def is_5g_enabled(self) -> bool:
        """
        :return: True/False
        """
        pass

    @abstractmethod
    def brand(self) -> str:
        """
        :return: brand of the smartphone
        """
        pass


class ProductFactory(ABC):
    """
    All factories should implement this interface
    """

    def __init__(self):
        self.factory = {}

    @abstractmethod
    def add_one_item(self, item_label: Any, item: Any) -> None:
        """
        add an item with item_label
        :param item_label:
        :param item:
        :return:
        """
        pass

    @abstractmethod
    def add_all_item(self) -> None:
        """
        Add all the items in one-shot by calling this method (see the implementation of FruitFactory,SmartPhoneFactory, AllProductFactory)
        :return:
        """
        pass

    @abstractmethod
    def is_item_available(self, item_label: Any) -> bool:
        """
        check if item is available in our factory or not
        :param item_label:
        :return: True/False
        """
        pass

    @abstractmethod
    def get_item(self, item_label: Any) -> Optional:
        """
        If item is available then return the actual instance of the corresponding item otherwise return None
        :param item_label:
        :return: Instance / None
        """
        pass

    @abstractmethod
    def get_item_template(self, item_label: Any) -> Optional:
        """
        If item is available then return the template of the corresponding item otherwise return None
        :param item_label:
        :return: Instance / None
        """
        pass


class Wallet(ABC):
    @abstractmethod
    def get_wallet_balance(self) -> float:
        pass

    def set_wallet_balance(self, new_balance: float) -> None:
        pass

    @abstractmethod
    def get_wallet_owner_name(self) -> str:
        pass

