from word_count import count_words


def test_count_words_basic():
    assert count_words("hello world") == {"hello": 1, "world": 1}


def test_count_words_case_insensitive():
    assert count_words("Cat cat CAT") == {"cat": 3}


def test_count_words_with_punctuation():
    assert count_words("Cat, cat! Dog.") == {"cat": 2, "dog": 1}


def test_count_words_empty_string():
    assert count_words("") == {}
