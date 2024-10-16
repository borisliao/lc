from collections import Counter


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


def review5(s: str, k: int) -> int:
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


def review10(s: str, k: int) -> int:
    """
    Anki 1-28-24
    Time: 16 min
    Used: Solution 1
    """
    l = 0
    letters = Counter()
    max_occurances = 0

    for r in range(len(s)):
        letters[s[r]] += 1
        most_occurances = max(letters.values())
        if (r+1-l) - most_occurances > k:
            letters[s[l]] -= 1  # s1
            l += 1
        max_occurances = max(max_occurances, (r+1-l))

    return max_occurances


def review11(s: str, k: int) -> int:
    """
    Mochi 4-15-24
    Time: 12:40, 5:27
    """
    count = {}
    l = 0
    chars = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        max_chars = max(count.values())
        length = r+1-l
        while length - max_chars > k:
            count[s[l]] -= 1
            l += 1
            max_chars = max(count.values())
            length = r+1-l
        chars = max(chars, length)
    return chars


def review12(s: str, k: int) -> int:
    """
    Mochi 10-9-24
    """
#   Input: s = "AABABBA", k = 1
#   Output: 4
    window = {}
    # A: 3
    # B: 1
    result = 0

    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        lenOfWindow = r+1-l  # 0 + 4 + 1 = 5
        maxValue = max(window.values())  # 3
        while lenOfWindow - maxValue > k:  # 5 - 3 <= 1
            window[s[l]] -= 1
            l += 1
            maxValue = max(window.values())
            lenOfWindow = r+1-l

        result = max(lenOfWindow, result)

    return result


def review13(s: str, k: int) -> int:
    """
    Mochi 10-13-24
    """
    window = Counter()
    result = 0
    l = 0
    for r in range(len(s)):
        window[s[r]] += 1
        while r+1-l - max(window.values()) > k:
            window[s[l]] -= 1
            l += 1
        result = max(result, r+1-l)
    return result


def review14(s: str, k: int) -> int:
    """
    Mochi 10-15-24
    """
    count = {0: 0}
    l = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        while r+1-l-max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r+1-l)

    return res
