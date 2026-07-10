from is_prime import is_prime


def test_smallest_prime():
    assert is_prime(2) is True


def test_odd_primes():
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True


def test_large_prime():
    assert is_prime(17) is True
    assert is_prime(19) is True


def test_composite_numbers():
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(100) is False


def test_one():
    assert is_prime(1) is False


def test_zero():
    assert is_prime(0) is False


def test_negative_numbers():
    assert is_prime(-1) is False
    assert is_prime(-2) is False
    assert is_prime(-5) is False
    assert is_prime(-17) is False
