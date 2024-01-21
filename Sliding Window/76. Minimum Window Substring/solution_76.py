from collections import Counter
from functools import reduce


# def minWindow(s: str, t: str) -> str:
#     """
#     Anki 1-19-24
#     Used: [Minimum Window Substring - Airbnb Interview Question - Leetcode 76](https://www.youtube.com/watch?v=jSto0O4AJbM)
#     """
#     l = 0
#     shortest = ""

#     matches = 0
#     s_count = Counter(s[:len(t)])
#     t_count = Counter(t)

#     for c, c_amount in s_count.items():
#         matches += 1 if t_count[c] <= c_amount else 0

#     if s_count == t_count:  # d5 len(t)
#         return s[:len(t)]

#     for r in range(len(t), len(s)):
#         s_count[s[r]] += 1
#         matches += 1 if s_count[s[r]] == t_count[s[r]] else 0  # d6 ==

#         while matches >= len(t_count):  # d5 len(t)
#             if shortest == "" or len(shortest) > r-l+1:
#                 shortest = s[l:r+1]  # d1 ==

#             matches -= 1 if s_count[s[l]] == t_count[s[l]] else 0  # d4 ^1
#             s_count[s[l]] -= 1
#             l += 1
#             # d2 s_count[s[l]] += 1
#             # d3 matches += 1 if s_count[s[l]] == t_count[s[l]] else 0

#     return shortest


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


# def review2(s: str, t: str) -> str:
#     """
#     Anki 1-20-24
#     """
#     result = ""
#     l = 0
#     t_count = Counter(t)
#     w_count = Counter()
#     have = 0
#     need = len(t_count)

#     for r in range(len(s)):
#         w_count[s[r]] += 1
#         if w_count[s[r]] == t_count[s[r]]:
#             have += 1

#         while have == need:
#             if result == "" or len(result) > r+1-l:  # d3 r-l
#                 result = s[l:r+1]  # s2 s[l:r]
#             w_count[s[l]] -= 1  # s1 w_count[l]
#             if w_count[s[l]] == t_count[s[l]]:
#                 have -= 1
#             l += 1

#     return result


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


# def review4(s: str, t: str) -> str:
#     """
#     Anki 1-20-24
#     Time: 20 min
#     """
#     pass
