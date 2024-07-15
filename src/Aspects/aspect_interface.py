from abc import ABCMeta, abstractmethod
from typing import Any

from src.use_case_interface import UseCaseInterface


class AspectInterface(UseCaseInterface, metaclass=ABCMeta):
    def __init__(self, use_case: UseCaseInterface):
        self.use_case: UseCaseInterface = use_case

    def preform_use_case(self) -> Any:
        return self.aspect_logic_implementation() + "\n" + self.use_case.preform_use_case()

    @abstractmethod
    def aspect_logic_implementation(self):
        pass
