from typing import Optional

from creational.abstract_factory.Implementation.fruits import FruitFactory, FruitLabel
from creational.abstract_factory.Implementation.smart_phone import SmartPhoneFactory, SmartPhoneLabel
from creational.abstract_factory.interfaces import ProductFactory
from enum import Enum
from itertools import chain

AllProductLabel = Enum(
    "AllProductLabel",
    [(label.name, label.value) for label in set(chain(SmartPhoneLabel, FruitLabel))]
)  # combine all the available labels in SmartPhone and Fruit


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
                                                                        SmartPhoneFactory)]  # Note that we registered the class instance not the class template
        for factory_label, factory in all_factories:
            self.add_one_item(factory_label, factory)

    def _get_factory_label(self, product_label: AllProductLabel) -> Optional:
        """
        Internal method to search for factory based on the product label
        :param product_label:
        :return: if product_label is present in some factory then return the corresponding factory_label otherwise None
        """
        for factory_label, factory in self.all_factories.items():
            if product_label in factory:
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
