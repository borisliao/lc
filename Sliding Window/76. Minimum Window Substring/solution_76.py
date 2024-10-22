from collections import Counter
from functools import reduce


def minWindow_neetcode(s: str, t: str) -> str:
    """
    Anki 1-19-24
    Used: [Minimum Window Substring - Airbnb Interview Question - Leetcode 76](https://www.youtube.com/watch?v=jSto0O4AJbM)
    """
    if t == '':
        return ''

    countT = Counter(t)
    window = Counter()

    have, need = 0, len(countT)
    result, result_len = [-1, -1], float('inf')

    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] += 1

        if window[c] == countT[c]:
            have += 1

        while have == need:
            if r-l+1 < result_len:
                result = [l, r]
                result_len = r-l+1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = result
    return s[l:r+1] if result_len != float('inf') else ""


def review1(s: str, t: str) -> str:
    """
    Anki 1-20-24
    Used: [Minimum Window Substring - Airbnb Interview Question - Leetcode 76](https://www.youtube.com/watch?v=jSto0O4AJbM)
    Time: 40 min
    O(n^2)
    """
    shortest = ''
    l = 0
    s_count = Counter()
    t_count = Counter(t)

    for r in range(len(s)):
        s_count[s[r]] += 1

        def contains_count():
            for t in t_count:
                if s_count[t] < t_count[t]:
                    return False
            return True

        while contains_count():
            if shortest == '' or len(shortest) > r+1-l:
                shortest = s[l:r+1]
            s_count[s[l]] -= 1
            l += 1

    return shortest


def review2(s: str, t: str) -> str:
    """
    Anki 1-20-24
    Time: 20 min
    Used: Solution 2, debugger 2
    """
    result = ""
    l = 0
    t_count = Counter(t)
    w_count = Counter()
    matches = 0
    for r in range(len(s)):
        w_count[s[r]] += 1
        if w_count[s[r]] == t_count[s[r]]:
            matches += 1

        while matches == len(t_count):
            if result == "" or len(result) > r+1-l:  # d3 r-l
                result = s[l:r+1]  # s2 s[l:r]
            if w_count[s[l]] == t_count[s[l]]:
                matches -= 1
            w_count[s[l]] -= 1  # s1 w_count[l], d4 down2
            l += 1

    return result


def review3(s: str, t: str) -> str:
    """
    Anki 1-20-24
    Time: 20 min
    """
    result = ""
    l = r = 0
    window_count = Counter()
    t_count = Counter(t)

    while r < len(s):
        window_count[s[r]] += 1

        def t_in_window():
            for c in t_count:
                if window_count[c] < t_count[c]:
                    return False
            return True

        while t_in_window():
            if result == '' or len(result) > r+1-l:
                result = s[l:r+1]
            window_count[s[l]] -= 1
            l += 1
        r += 1

    return result


def review4(s: str, t: str) -> str:
    """
    Anki 1-26-24
    Used: Debugger 5
    Time: 31 min
    """
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1
    w_count = {}

    matches = 0
    min_substring = ''
    l = 0
    r = 0
    for r in range(len(s)):  # d3
        w_count[s[r]] = w_count.get(s[r], 0) + 1
        if t_count.get(s[r], 0) == w_count[s[r]]:  # d4 t_count[s[r]]
            matches += 1

        # d3 r += 1  # d1, d2 up 7

        if r+1-l < len(t):
            continue

        while matches == len(t_count):
            if min_substring == '' or len(min_substring) > len(s[l:r+1]):
                min_substring = s[l:r+1]
            if w_count[s[l]] == t_count.get(s[l], 0):  # d5 t_count[s[l]]
                matches -= 1
            w_count[s[l]] -= 1
            l += 1

    return min_substring


def review5(s: str, t: str) -> str:
    """
    Anki 2-3-24
    Time: 20 min
    Used: Debugger 2, solution 2
    """
    result = ''
    l = 0
    S = Counter()
    T = Counter(t)
    matches = 0

    for r, c in enumerate(s):
        S[c] += 1  # s2 S[r]
        if S[c] == T[c]:
            matches += 1

        while matches == len(T):
            if result == '' or len(result) > r+1-l:
                result = s[l:r+1]  # d1 result =, d3 result[l:r+1]

            if T[s[l]] == S[s[l]]:
                matches -= 1
            S[s[l]] -= 1  # s3
            l += 1
    return result


def review6(s: str, t: str) -> str:
    """
    Anki 2-3-24
    Time: 14:45
    Used: solution 2
    """
    result = ''
    l = 0
    t_count = Counter(t)
    window = Counter()

    for r in range(len(s)):
        window[s[r]] += 1

        def t_in_window():
            for c in t_count:
                if t_count[c] > window[c]:
                    return False
            return True

        while t_in_window():
            if result == '' or len(result) > r+1-l:
                result = s[l:r+1]
            window[s[l]] -= 1  # s1 left 1, s2 window[l]
            l += 1  # s1 left 1

    return result


def review7(s: str, t: str) -> str:
    """
    Anki 2-4-24
    Time: 13 min
    """
    count = Counter(t)
    window = Counter()
    l = 0
    result = ''

    for r, c in enumerate(s):
        window[c] += 1

        def inCount():
            for char in count:
                if window[char] < count[char]:
                    return False
            return True

        while inCount():  # gpt2 if
            if result == '' or len(result) > r+1-l:
                result = s[l:r+1]
            window[s[l]] -= 1  # d1 window[l]
            l += 1

    return result


def review8(s: str, t: str) -> str:
    """
    Anki 2-5-24
    Time: 12 min
    """
    t_count = Counter(t)
    window = Counter()
    matches = 0
    l = 0
    result = ''

    for r, c in enumerate(s):
        window[c] += 1
        if window[c] == t_count[c]:
            matches += 1

        while len(t_count) == matches:
            if result == '' or r+1-l < len(result):
                result = s[l:r+1]
            if window[s[l]] == t_count[s[l]]:  # s1 up 2 and !=
                matches -= 1
            window[s[l]] -= 1
            l += 1
    return result


def review9(s: str, t: str) -> str:
    """
    Anki 2-13-24
    Used: debugger 1
    Time: 15 min
    """
    result = ''
    t_count = Counter(t)
    window = Counter()
    matches = 0

    l = 0

    for r, c in enumerate(s):
        window[c] += 1

        if window[c] == t_count[c]:
            matches += 1

        while matches == len(t_count):  # d1 if
            if result == '' or len(result) > r+1-l:
                result = s[l:r+1]

            if window[s[l]] == t_count[s[l]]:
                matches -= 1
            window[s[l]] -= 1
            l += 1

    return result


def review10(s: str, t: str) -> str:
    """
    Mochi 10-3-24
    """
    l = 0
    substring = Counter(t)
    window = Counter()

    smallest = ''

    for r in range(len(s)):
        window[s[r]] += 1

        while window >= substring:
            if smallest == '' or (r+1-l) <= len(smallest):
                smallest = s[l:r+1]
            window[s[l]] -= 1
            l += 1

    return smallest


def review11(s: str, t: str) -> str:
    """
    Mochi 10-21-24
    """
    count = {}
    for c in t:
        count[c] = count.get(c, 0) + 1

    result = ''

    window = {}
    l = 0
    r = 0

    while r < len(s):
        window[s[r]] = window.get(s[r], 0) + 1

        match = True
        while match:
            for c in count:
                if c in window and window[c] == count[c]:
                    pass
                else:
                    match = False
                    break
            if match:
                if result == '' or len(result) > r+1-l:
                    result = s[l:r+1]
                window[s[l]] -= 1
                l += 1
        r += 1

    return result
