# def naive(s: str, t: str) -> bool:
#     if len(s) != len(t): return False

#     for letter in t:
#         if letter not in s:
#             return False

#     return True

from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dictS = {}

    for char in s:
        if char in dictS:
            dictS[char] += 1
        else:
            dictS[char] = 1

    for char in t:
        if char in dictS:
            if dictS[char] == 1:
                del dictS[char]
            else:
                dictS[char] -= 1

    return False if len(dictS) > 0 else True


def review1(s: str, t: str) -> bool:
    """Anki Review 10/28/23"""
    # key: letter
    # value: amount of letters counted so far
    count: dict[str, int] = defaultdict(lambda: 0)

    # optimization: length not equal means not anagram
    if len(s) != len(t):
        return False

    for c in s:
        count[c] += 1

    for c in t:
        count[c] -= 1

        # optimization: < 0 means it the length will always be at least 1 (therefore not anagram)
        if count[c] < 0:
            return False

        if count[c] == 0:
            del count[c]

    if len(count) == 0:
        return True

    return False


def review2(s: str, t: str) -> bool:
    """
    Anki 11/14/23
    Used: debugger (4)
    Time: 9 min
    """
    s_set = defaultdict(lambda: 0)
    for c in s:
        s_set[c] += 1  # debugger (1)

    for c in t:  # debugger (1) conceptual (used set instead of counting instances)
        # debugger (1) conceptual (did not need to check if c existed in s_set)
        s_set[c] -= 1  # debugger (1)
        if s_set[c] < 0:
            return False
        if s_set[c] == 0:
            del s_set[c]

    return True if len(s_set) == 0 else False


def review3(s: str, t: str) -> bool:
    """
    Anki 11-29-23
    Time: 19:59
    """
    s_count = defaultdict(lambda: 0)

    for c in s:
        s_count[c] += 1

    for c in t:
        if s_count[c] == 1:
            del s_count[c]
        else:
            s_count[c] -= 1

    return True if len(s_count) == 0 else False


def review4(s: str, t: str) -> bool:
    """
    Mochi 4-24-24
    """
    sCount = {}
    for c in s:
        sCount[c] = 1 + sCount.get(c, 0)

    tCount = {}
    for c in t:
        if c not in sCount:
            return False
        tCount[c] = 1 + tCount.get(c, 0)

    return sCount == tCount
