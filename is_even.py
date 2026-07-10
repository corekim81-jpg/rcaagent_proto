def is_even(n: int) -> bool:
    """Return True if n is even, False if n is odd.

    Handles negative numbers correctly (e.g. -4 is even, -3 is odd).
    """
    return n % 2 == 0
