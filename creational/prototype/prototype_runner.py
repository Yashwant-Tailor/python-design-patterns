from typing import Any

from creational.abstract_factory.abstract_factory_runner import Shop, Customer, AllProductFactory, FruitLabel
from creational.prototype.interfaces import Prototype


class ShopCloneable(Shop, Prototype):
    def __init__(self, name: str, factory=None):
        super().__init__(name, factory)

    def clone(self, new_shop_name: str) -> Any:
        return ShopCloneable(new_shop_name, self.factory)

if __name__ == "__main__":
    store = ShopCloneable("PrototypePythonItemFactory", AllProductFactory())
    store.add_all_item()
    memba = Customer("Memba", 4000)

    if store.can_buy(memba, FruitLabel.orange):
        fruit = store.buy(memba, FruitLabel.orange)
    if store.can_buy(memba, FruitLabel.apple):
        fruit = store.buy(memba, FruitLabel.apple)

    another_store = store.clone("AnotherPrototypePythonItemFactory")  # now we don't need to set the factories for this store as it is exact copy of our store
    bhawa = Customer("bhawa", 5000)

    if another_store.can_buy(bhawa, FruitLabel.orange):
        fruit = another_store.buy(bhawa, FruitLabel.orange)
    if another_store.can_buy(bhawa, FruitLabel.apple):
        fruit = another_store.buy(bhawa, FruitLabel.apple)
