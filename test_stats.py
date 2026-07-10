import pytest
from stats import average, median


def test_average_normal_case():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_with_floats():
    assert average([1.5, 2.5, 3.0]) == pytest.approx(2.333333333333333)


def test_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])


def test_median_odd_number_of_elements():
    assert median([1, 2, 3]) == 2


def test_median_odd_with_floats():
    assert median([1.5, 2.5, 3.5]) == 2.5


def test_median_even_number_of_elements():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_even_with_floats():
    assert median([1.5, 2.5, 3.5, 4.5]) == 3.0


def test_median_single_element():
    assert median([5]) == 5


def test_median_single_element_float():
    assert median([3.14]) == 3.14


def test_median_empty_list_raises_error():
    with pytest.raises(ValueError):
        median([])


def test_median_with_negative_numbers():
    assert median([-3, -1, 0, 1, 3]) == 0


def test_median_with_duplicates():
    assert median([1, 2, 2, 2, 3]) == 2


def test_median_unordered_list():
    assert median([3, 1, 2]) == 2


def test_median_even_unordered():
    assert median([4, 1, 3, 2]) == 2.5
