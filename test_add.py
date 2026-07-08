from add import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, 1) == 0


def test_add_both_negative():
    assert add(-5, -3) == -8


def test_add_zero():
    assert add(0, 0) == 0


def test_add_with_zero():
    assert add(5, 0) == 5
    assert add(0, -3) == -3
