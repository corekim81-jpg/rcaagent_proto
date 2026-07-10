from palindrome import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_simple_non_palindrome():
    assert is_palindrome("hello") is False


def test_ignores_case():
    assert is_palindrome("RaceCar") is True


def test_ignores_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_sentence_with_punctuation_that_is_not_palindrome():
    assert is_palindrome("Was it a car or a cat I saw") is True
    assert is_palindrome("This is not a palindrome!") is False


def test_empty_string_is_palindrome():
    assert is_palindrome("") is True


def test_single_character_is_palindrome():
    assert is_palindrome("a") is True
