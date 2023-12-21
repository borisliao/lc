from collections import Counter, defaultdict


def characterReplacement(s: str, k: int) -> int:
    count = {}

    length = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        length = max(length, r-l+1)

    return length


def maxValue(s: str, k: int) -> int:
    count = {}

    maxValue = 0
    length = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxValue = max(maxValue, count[s[r]])

        while (r-l+1) - maxValue > k:
            count[s[l]] -= 1
            l += 1

        length = max(length, r-l+1)

    return length


# def review1(s: str, k: int) -> int:
#     """
#     Anki 12-21-23
#     Time: 38:10
#     Used: Debugger 4
#     Not preformant
#     """
#     length = 0
#     l = 0
#     r = 1

#     while r <= len(s):
#         count = Counter(s[l:r])

#         if len(count) <= 1:
#             length = max(length, len(s[l:r]))  # d1
#             r += 1
#             continue

#         most_count = 0
#         for c, o in count.items():
#             most_count = max(most_count, o)

#         if r-l - most_count > k:
#             l += 1
#             continue

#         length = max(length, len(s[l:r]))
#         r += 1

#     return length

def review2(s: str, k: int) -> int:
    """
    12-21-23
    """
    l = 0
    count = {}
    length = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        if r-l+1 - max(count.values()) > k:  # d3 r-l-1
            count[s[l]] -= 1  # d1
            l += 1
        length = max(length, r-l+1)  # d2 r-l-1

    return length


# def review3(s: str, k: int) -> int:
#     """
#     Anki
#     """
