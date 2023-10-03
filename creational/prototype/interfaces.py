from abc import ABC, abstractmethod
from typing import Any


class Prototype(ABC):
    @abstractmethod
    def clone(self,clone_param:Any) -> Any:
        pass
