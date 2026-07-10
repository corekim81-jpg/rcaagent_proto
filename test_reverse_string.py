from reverse_string import reverse_string


def test_reverse_string_normal_word():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_sentence_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_string_empty_string():
    assert reverse_string("") == ""


def test_reverse_string_single_character():
    assert reverse_string("a") == "a"


def test_reverse_string_palindrome_like_string():
    # "abcba" reversed is still "abcba" - this is just a coincidence of
    # reversal, not special palindrome handling.
    assert reverse_string("abcba") == "abcba"
    # A stronger check that only plain reversal happens, no special-casing:
    assert reverse_string("abccba") == "abccba"
    assert reverse_string("abcxba") == "abxcba"
