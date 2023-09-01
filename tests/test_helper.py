import pytest

from examples.src.utils.helper import is_greater_than, suma


def test_when_sum_to_numbers_then_result_is_retrieved():  # noqa: ANN201
    assert suma(2, 3) == 5  # add assertion here  # noqa: S101


def test_when_compare_two_numbers_then_true_flags_retrieved_if_first_values_is_geather_than_second_value():  # noqa: ANN201
    assert is_greater_than(5, 2) is True  # noqa: S101


def test_when_compare_two_numbers_then_false_flags_retrieved_if_second_values_is_geather_than_first_value():  # noqa: ANN201
    assert is_greater_than(2, 5) is False  # noqa: S101


@pytest.mark.parametrize(
    "input_x, input_y, expected_value",  # noqa: PT006
    [
        (2, 3, 5),
        (5, -3, 2),
    ],
)
def test_when_suma_with_parameters(input_x: int, input_y: int, expected_value: int):  # noqa: ANN201
    assert suma(input_x, input_y) == expected_value  # noqa: S101
