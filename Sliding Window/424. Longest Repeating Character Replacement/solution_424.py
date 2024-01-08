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


def review3(s: str, k: int) -> int:
    """
    Anki 12-21-23
    Time: 30 min
    Used: debugger 3
    """
    l = 0
    count = {}

    max_window_size = 0
    for r in range(len(s)):  # d2 len(s)+1
        count[s[r]] = count.get(s[r], 0) + 1

        window_size = len(s[l:r+1])  # d2 len(s[l:r])
        if window_size - max(count.values()) > k:  # d1 len(window_size)
            count[s[l]] -= 1
            l += 1
            window_size -= 1  # d3

        max_window_size = max(max_window_size, window_size)

    return max_window_size


def review4(s: str, k: int) -> int:
    """
    Anki 12-21-23
    Time: 14 min
    Used: Debugger 1
    """
    count = {}
    length = 0
    l = 0
    maxF = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        maxF = max(maxF, max(count.values()))

        if r+1-l - maxF > k:
            count[s[l]] -= 1
            l += 1  # d1 l -= 1

        length = max(length, r+1-l)

    return length


def review4(s: str, k: int) -> int:
    """
    Anki 12-24-23
    Time: 8 min
    Used: debugger 2
    O(26 * n)
    """
    l = 0
    count = Counter()
    max_length = 0

    for r in range(len(s)):
        count[s[r]] += 1
        if r+1-l - max(count.values()) > k:  # d1
            count[s[l]] -= 1  # d2
            l += 1
        max_length = max(max_length, r+1-l)

    return max_length


# def review5(s: str, k: int) -> int:
#     """
#     Anki 12-31-23
#     """
#     l = 0
#     r = 0
#     count = defaultdict(lambda: 0)
#     longest = 0

#     while r <= len(s):
#         occurances = max(count.values() if count else [0])
#         if occurances + k >= r-l:
#             longest = r-l
#             r += 1
#             if r < len(s):
#                 count[s[r]] += 1
#         else:
#             count[s[l]] -= 1
#             l += 1

#     return longest

def review6(s: str, k: int) -> int:
    """
    Anki 12-31-23
    Used: Solution
    Time: 50 min
    """
    count = {}
    l = 0
    largest = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        if r+1-l - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1  # d1 l -= 1

        largest = max(largest, r+1-l)

    return largest


# def review6(s: str, k: int) -> int:
#     """
#     Anki 12-31-23
#     Time: 4 min
#     """
#     count = {}
#     l = 0
#     longest = 0

#     for r in range(len(s)):
#         count[s[r]] = count.get(s[r], 0) + 1

#         if max(count.values()) + k <= r+1-l: # you need to fix the l-r window range first before computing the longest
#             longest = max(longest, r+1-l)
#         else:
#             count[s[l]] -= 1
#             l += 1

#     return longest


def review7(s: str, k: int) -> int:
    """
    Anki 12-31-23
    Time: 7 min
    Used: Solution 1
    """
    count = {}
    l = 0
    longest = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        if r+1-l - max(count.values()) > k:
            count[s[l]] -= 1  # s1
            l += 1
        longest = max(longest, r+1-l)

    return longest


def review8(s: str, k: int) -> int:
    """
    Anki 1-1-24
    Time: 20 min
    """
    count = {}
    l = 0
    longest = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        if max(count.values()) + k < r+1-l:
            count[s[l]] -= 1
            l += 1
        longest = max(longest, r+1-l)

    return longest


def review9(s: str, k: int) -> int:
    """
    Anki 1-7-24
    Time: 8 min
    """
    count = {}
    l = 0
    longest = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        if r+1-l - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        longest = max(longest, r+1-l)

    return longest
