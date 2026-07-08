import pytest
from stats import average


def test_average_normal_case():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_with_floats():
    assert average([1.5, 2.5, 3.0]) == pytest.approx(2.333333333333333)


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])
