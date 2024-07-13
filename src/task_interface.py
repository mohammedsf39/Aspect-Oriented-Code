from abc import ABCMeta, abstractmethod
from typing import Any


class TaskInterface(metaclass=ABCMeta):
    @abstractmethod
    def preform_task(self) -> Any:
        pass
