from abc import ABCMeta, abstractmethod
from typing import Any


class UseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def preform_use_case(self) -> Any:
        pass
