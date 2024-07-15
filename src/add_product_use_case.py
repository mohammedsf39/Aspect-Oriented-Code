from typing import Any

from src.use_case_interface import UseCaseInterface


class AddProductUseCase(UseCaseInterface):
    def preform_use_case(self) -> Any:
        return "Product added successfully!"
