from src.Aspects.authentication_aspect import AuthenticationAspect
from src.Aspects.logging_aspect import LoggingAspect
from src.add_product_task import AddProductTask


def test_add_product_should_return_product_added():
    task = AddProductTask()
    assert task.preform_task() == "Product added successfully!"


def test_add_product_should_check_authentication():
    task = AddProductTask()
    aspect = AuthenticationAspect(task)
    assert aspect.preform_task() == "User has privileges.\nProduct added successfully!"


def test_add_product_should_log_and_check_authentication():
    task = AddProductTask()
    aspect = AuthenticationAspect(task)
    aspect = LoggingAspect(aspect)
    assert (
        aspect.preform_task()
        == "Logging ... User wants to add a product.\nUser has privileges.\nProduct added successfully!"
    )
