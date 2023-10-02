from creational.abstract_factory.interfaces import SmartPhone, ProductFactory
from enum import Enum
from typing import Optional, Any


class SmartPhoneLabel(Enum):
    mamsung = "Mamsung"
    aphone = "aPhone"
    zeroplus = "ZeroPlus"
    random_smart_phone = "random_smart_phone"


class SmartPhoneFactory(ProductFactory):
    """
    NOTE : In this factory we will register all the smartphone product templates
    """

    def add_one_item(self, smart_phone_label: SmartPhoneLabel, smart_phone: SmartPhone) -> None:
        """

        :param smart_phone_label:
        :param smart_phone:
        :return:
        """
        self.factory[smart_phone_label] = smart_phone

    def add_all_item(self) -> None:
        """
        For now the implementation is static (we have hardcoded all the smartphone template needs to be added , but it can
        be dynamic where we will pass all the smartphone template needs to be added in this factory)
        :return:
        """
        print("Adding all the smart-phones")
        all_fruits = [(SmartPhoneLabel.mamsung, Mamsung), (SmartPhoneLabel.aphone,
                                                           aPhone)]  # Note that we only registered the class template not the instance of the class
        for smart_phone_label, fruit in all_fruits:
            self.add_one_item(smart_phone_label, fruit)

    def is_item_available(self, smart_phone_label: Any) -> bool:
        """
        check that the smartphone is available to this corresponding smart_phone_label
        :param smart_phone_label:
        :return: True/False
        """
        return smart_phone_label in self.factory

    def get_item(self, smart_phone_label: SmartPhoneLabel) -> Optional:
        """
        Get the actual instance of the smartphone if smart_phone_label is present in our factory otherwise return None
        :param smart_phone_label:
        :return:
        """
        if smart_phone_label in self.factory:
            return self.factory[smart_phone_label]()
        return None

    def get_item_template(self, smart_phone_label: SmartPhoneLabel) -> Optional:
        """
        Get the template of the smartphone if smart_phone_label is present in our factory otherwise return None
        :param smart_phone_label:
        :return:
        """
        if smart_phone_label in self.factory:
            return self.factory[smart_phone_label]
        return None


class Mamsung(SmartPhone):
    def name(self) -> str:
        return "Mamsung"

    def category(self) -> str:
        return SmartPhone.category() + " -> Mamsung"

    @staticmethod
    def price() -> float:
        return 3029.38

    def shape(self) -> str:
        return "Z shape"

    def brand(self) -> str:
        return "Mamsung (Mouth Morea)"

    def battery(self) -> str:
        return "5500mh"

    def is_5g_enabled(self):
        return True


class aPhone(SmartPhone):
    def name(self) -> str:
        return "aPhone"

    def category(self) -> str:
        return SmartPhone.category() + " -> aPhone"

    @staticmethod
    def price() -> float:
        return 189289.38  # a number you can't afford

    def shape(self) -> str:
        return "Rectangle"

    def brand(self) -> str:
        return "aPhone"

    def battery(self) -> str:
        return "6000mh"

    def is_5g_enabled(self):
        return False
