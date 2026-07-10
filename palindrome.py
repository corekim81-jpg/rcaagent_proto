def is_palindrome(text: str) -> bool:
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
