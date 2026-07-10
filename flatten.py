def flatten(nested: list) -> list:
    """Flatten a nested list of arbitrary depth into a single-level list.

    Args:
        nested: A list that may contain nested lists at any depth.

    Returns:
        A single-level list containing all elements from the input,
        with all nesting removed.

    Example:
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten([])
        []
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
