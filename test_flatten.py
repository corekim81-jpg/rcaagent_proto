from flatten import flatten


def test_flatten_basic():
    """Flatten a list with multiple levels of nesting."""
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_empty():
    """Flatten an empty list."""
    assert flatten([]) == []


def test_flatten_already_flat():
    """Flatten a list that is already flat."""
    assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_flatten_single_nested():
    """Flatten a list with single-level nesting."""
    assert flatten([1, [2], [3]]) == [1, 2, 3]


def test_flatten_deeply_nested():
    """Flatten deeply nested lists."""
    assert flatten([[[[[1]]]], 2, [3, [4, [5, [6]]]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_with_empty_nested():
    """Flatten lists containing empty nested lists."""
    assert flatten([1, [], [2, []], 3]) == [1, 2, 3]


def test_flatten_all_empty_nested():
    """Flatten a list of only empty nested lists."""
    assert flatten([[], [[]], [[[]]]]) == []


def test_flatten_strings_as_elements():
    """Flatten lists with strings as elements."""
    assert flatten(['a', ['b', 'c'], ['d', ['e', 'f']]]) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_flatten_mixed_types():
    """Flatten lists with mixed types."""
    assert flatten([1, 'a', [2, 'b'], [3, [4, 'c']]]) == [1, 'a', 2, 'b', 3, 4, 'c']
