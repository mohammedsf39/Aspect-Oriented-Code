from src.Aspects.authentication_aspect import AuthenticationAspect
from src.Aspects.logging_aspect import LoggingAspect
from src.add_product_task import AddProductUseCase


def test_add_product_should_return_product_added():
    task = AddProductUseCase()
    assert task.preform_use_case() == "Product added successfully!"


def test_add_product_should_check_authentication():
    task = AddProductUseCase()
    aspect = AuthenticationAspect(task)
    assert aspect.preform_use_case() == "User has privileges.\nProduct added successfully!"


def test_add_product_should_log_and_check_authentication():
    task = AddProductUseCase()
    aspect = AuthenticationAspect(task)
    aspect = LoggingAspect(aspect)
    assert (
        aspect.preform_use_case()
        == "Logging ... User wants to add a product.\nUser has privileges.\nProduct added successfully!"
    )
