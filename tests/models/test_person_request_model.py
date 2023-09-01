import pytest
from pydantic import ValidationError

from examples.src.models.person_request_model import PersonRequestModel


def test_when_values_are_given_and_they_are_valid_then_values_are_retrieved() -> None:
    current = PersonRequestModel(
        username="grleyva2023",
        email="email@gmail.com",
    )

    assert current.username == "grleyva2023"
    assert current.email == "email@gmail.com"


def test_when_username_is_not_given_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(email="email@gmail.com")


def test_when_username_is_blank_given_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(username="", email="email@gmail.com")


def test_when_username_is_invalid_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(username="grleyva", email="email")


def test_when_email_is_not_given_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(username="grleyva2023")


def test_when_email_is_blank_given_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(username="grleyva2023", email="")


def test_when_email_is_invalid_then_error_is_thrown() -> None:
    with pytest.raises(ValidationError):
        PersonRequestModel(username="grleyva2023", email="email")

# comprobar que se lanza exeception es como un assertDoesThrown
def test_when_email_is_invalid_then_error_is_thrown_with_try() -> None:
    try:
        PersonRequestModel(username="grleyva2023", email="email")
        raise AssertionError
    except ValidationError:
        assert True


# comprobar que no se lanza exeception es como un assertDoesNotThrown
def test_when_email_is_invalid_then_error_is_thrown_with_tryvv() -> None:
    try:
        PersonRequestModel(username="grleyva2023", email="email@email.co")
        assert True
    except ValidationError:
        raise AssertionError


# al invocar un metodo q pude devolver excepcion, cuando queremos hacer el when retorne Excepcion
# def test_exception():
#     with pytest.raises(Exception) as excinfo:

# https://pytest-with-eric.com/introduction/pytest-assert-exception
# https://www.youtube.com/watch?v=5ufpsjfk99U
# https://www.youtube.com/watch?v=dWcC7Mhljos
