from abc import ABCMeta, abstractmethod
from typing import Any

from src.task_interface import TaskInterface


class AspectInterface(TaskInterface, metaclass=ABCMeta):
    def __init__(self, task: TaskInterface):
        self.task: TaskInterface = task

    def preform_task(self) -> Any:
        return self.aspect_task() + "\n" + self.task.preform_task()

    @abstractmethod
    def aspect_task(self):
        pass
