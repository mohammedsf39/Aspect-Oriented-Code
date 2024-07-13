from typing import Any

from src.task_interface import TaskInterface


class AddProductTask(TaskInterface):
    def preform_task(self) -> Any:
        return "Product added successfully!"
