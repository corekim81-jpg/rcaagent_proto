import string
from collections import Counter


def count_words(text: str) -> dict[str, int]:
    if not text:
        return {}

    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, " ")

    words = text.split()
    return dict(Counter(words))
