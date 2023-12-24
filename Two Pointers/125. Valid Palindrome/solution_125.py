def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def review1(s: str) -> bool:
    """
    Anki 12-24-23
    Used: Debugger 1
    Time: 27 min
    """
    l = 0
    r = len(s) - 1

    while l <= r:
        if not s[l].isalnum():  # d1 while to if
            l += 1
            continue
        if not s[r].isalnum():  # d1 while to if
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True
