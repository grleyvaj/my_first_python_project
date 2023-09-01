import pytest

from examples.src.utils.session import login


@pytest.mark.parametrize(
    "username, password, expected_value",  # noqa: PT006
    [
        ("gloria", "123", True),
        ("gloria", "::any::", False),
        ("::any::", "123", False),
        ("::any::", "::any::", False),
    ],
)
def test_when_credentials_are_correct_then_login_pass_with_parametrize(username: str, password: str, expected_value: bool) -> None:  # noqa: FBT001
    assert login(username, password) == expected_value  # noqa: S101


def test_when_credentials_are_correct_then_login_pass() -> None:
    assert login("gloria", "123")


def test_when_username_is_invalid_login_fail() -> None:
    assert not login("::any::", "123")


def test_when_password_is_invalid_login_fail() -> None:
    assert not login("gloria", "::any::")
