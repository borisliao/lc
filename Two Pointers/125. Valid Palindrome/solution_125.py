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


def review2(s: str) -> bool:
    """
    Anki 12-31-23
    Time: 7 min
    Used: debugger 1
    """
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] == ' ' or not s[l].isalnum():
            l += 1
            continue
        if s[r] == ' ' or not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False
        l += 1  # d1
        r -= 1  # d1

    return True


def review3(s: str) -> bool:
    """
    Anki 1-26-24
    Time: 6 min
    """
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():  # note: ' ' is not alnum
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True


def review4(s: str) -> bool:
    """
    Mochi 4-18-24
    """
    l = 0
    r = len(s)-1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True
