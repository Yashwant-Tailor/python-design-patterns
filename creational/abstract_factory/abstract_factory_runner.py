from typing import Optional, Any
from creational.abstract_factory.interfaces import ProductFactory, Wallet, ShopProduct
from creational.abstract_factory.Implementation.fruits import FruitFactory, FruitLabel
from creational.abstract_factory.Implementation.smart_phone import SmartPhoneFactory, SmartPhoneLabel
from enum import Enum
from random import choice as random_choice

# combine all the available labels in SmartPhone and Fruit
AllProductLabel = [label for label in SmartPhoneLabel]
AllProductLabel += [label for label in FruitLabel]


def get_random_product_label():
    return random_choice(AllProductLabel)


class FactoryLabel(Enum):
    """
    Enums to assign each product factory a label
    """
    fruit_factory = "FruitFactory"
    smart_phone_factory = "SmartPhoneFactory"


class AllProductFactory(ProductFactory):
    """
    NOTE : Here we will register all the product factories not the product templates
    """

    def __init__(self):
        self.all_factories = {}  # global factory to keep track of all product factories

    def add_one_item(self, factory_label: FactoryLabel, factory: ProductFactory) -> None:
        """
        Add one factory with a factory label
        :param factory_label:
        :param factory: factory (which follows the ProductFactory interface)
        :return:
        """
        self.all_factories[factory_label] = factory

    def add_all_item(self) -> None:
        """
        For now the implementation is static (we have hardcoded all the factories needs to be added , but it can
        be dynamic where we will pass all the factories needs to be added in this all product factory)
        :return:
        """
        all_factories = [(FactoryLabel.fruit_factory, FruitFactory()), (FactoryLabel.smart_phone_factory,
                                                                        SmartPhoneFactory())]  # Note that we registered the class instance not the class template
        for factory_label, factory in all_factories:
            self.add_one_item(factory_label, factory)
            # add all items available for each factory
            factory.add_all_item()

    def _get_factory_label(self, product_label: AllProductLabel) -> Optional:
        """
        Internal method to search for factory label based on the product label
        :param product_label:
        :return: if product_label is present in some factory then return the corresponding factory_label otherwise None
        """
        for factory_label, factory in self.all_factories.items():
            if factory.is_item_available(product_label):
                return factory_label
        return None

    def is_item_available(self, product_label: AllProductLabel) -> bool:
        """
        check in each individual factory that item is available or not
        :param product_label: product_label to search in our store
        :return: True/False
        """
        factory_label = self._get_factory_label(product_label)
        return True if factory_label is not None else False

    def get_item(self, product_label: AllProductLabel) -> Optional:
        """
        return the actual instance of the product (if not available then return None)
        :param product_label: product label to get the actual instance of product
        :return: Optional
        """
        factory_label = self._get_factory_label(product_label)
        if factory_label is not None:
            factory = self.all_factories[factory_label]
            return factory.get_item(product_label)
        return None

    def get_item_template(self, product_label: AllProductLabel) -> Optional:
        """
        return the template of the product (if not available then return None)
        :param product_label: product label to get the actual instance of product
        :return: Optional
        """
        factory_label = self._get_factory_label(product_label)
        if factory_label is not None:
            factory = self.all_factories[factory_label]
            return factory.get_item_template(product_label)
        return None


class ItemNotAvailableError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return repr(self)


class NotEnoughBalanceError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return repr(self)


class Shop():
    def __init__(self, name):
        self.shop_name = name
        self.factory = AllProductFactory()

    def add_all_item(self) -> None:
        self.factory.add_all_item()

    def _item_is_in_store(self, item_label: AllProductLabel) -> bool:
        if not self.factory.is_item_available(item_label):
            raise ItemNotAvailableError(f"{item_label.value} is not available in {self.shop_name}")
        return True

    @staticmethod
    def _customer_has_enough_balance(customer_wallet: Wallet, item: ShopProduct) -> bool:
        if customer_wallet.get_wallet_balance() < item.price():
            raise NotEnoughBalanceError(
                f"{customer_wallet.get_wallet_owner_name()} doesn't have the enough balance to buy {item.name()}")
        return True

    @staticmethod
    def _update_customer_balance(customer_wallet: Wallet, amount_to_deduct: float) -> None:
        curr_balance = customer_wallet.get_wallet_balance()
        new_balance = curr_balance - amount_to_deduct
        customer_wallet.set_wallet_balance(new_balance)

    def can_buy(self, customer_wallet: Wallet, item_label: Any):
        try:
            self._item_is_in_store(item_label)
            product_template = self.factory.get_item_template(item_label)
            self._customer_has_enough_balance(customer_wallet, product_template)
            return True
        except ItemNotAvailableError as e:
            print(e)
            return False
        except NotEnoughBalanceError as e:
            print(e)
            return False
        except Exception as e:
            raise e

    def buy(self, customer_wallet: Wallet, item_label: Any) -> Any:
        self._item_is_in_store(item_label)
        product_template = self.factory.get_item_template(item_label)
        self._customer_has_enough_balance(customer_wallet, product_template)
        product_price = product_template.price()
        self._update_customer_balance(customer_wallet, product_price)
        return self.factory.get_item(item_label)  # instantiation of actual class


class Customer(Wallet):
    def __init__(self, name: str, wallet_balance: float):
        self.name = name
        self.wallet_balance = wallet_balance

    def get_wallet_balance(self) -> float:
        return self.wallet_balance

    def set_wallet_balance(self, new_balance: float) -> None:
        self.wallet_balance = new_balance

    def get_wallet_owner_name(self) -> str:
        return self.name


store = Shop("PythonFruitFactory")
store.add_all_item()
memba = Customer("Memba", 4000)

if store.can_buy(memba, FruitLabel.orange):
    fruit = store.buy(memba, FruitLabel.orange)
if store.can_buy(memba, FruitLabel.apple):
    fruit = store.buy(memba, FruitLabel.apple)
