from is_even import is_even


def test_positive_even():
    assert is_even(4) is True


def test_positive_odd():
    assert is_even(3) is False


def test_zero():
    assert is_even(0) is True


def test_negative_even():
    assert is_even(-4) is True


def test_negative_odd():
    assert is_even(-3) is False
