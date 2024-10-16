from collections import Counter


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    length = 0

    L = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[L])
            L += 1

        seen.add(s[r])

        length = max(len(seen), length)

    return length


def neetcode(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


def review1(s: str) -> int:
    """
    Anki 12-19-23
    Used: Longest Substring Without Repeating Characters - Leetcode 3 - Python](https://www.youtube.com/watch?v=wiGpQwVHdE0)
    Time: 36:56
    """
    l = 0

    size = 0

    chars = set()
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        size = max(size, r-l+1)

    return size


def review2(s: str) -> int:
    """
    Anki 12-19-23
    Time: 12 min
    """
    l = 0
    chars = set()
    result = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        result = max(len(chars), result)

    return result


def review3(s: str) -> int:
    """
    Anki 12-24-23
    Used: debugger 1, insight 1
    Time: 12 min
    """
    l = 0
    characters = Counter()
    max_length = 0  # d2 float('inf')

    for r in range(len(s)):
        characters[s[r]] += 1

        while characters[s[r]] > 1:
            characters[s[l]] -= 1
            l += 1

        max_length = max(max_length, r+1-l)  # i1
        # max_length = max(max_length, characters.total())  # i1 characters.total(), but it's slower

    return max_length


def review4(s: str) -> int:
    """
    Anki 1-12-24
    """
    seen = set()
    l = 0
    largest = 0

    for r in range(len(s)):
        while s[r] in seen:  # d1
            seen.remove(s[l])
            l += 1
        largest = max(largest, r+1-l)
        seen.add(s[r])

    return largest


def review5(s: str) -> int:
    """
    Anki 1-14-24
    Time: 5 min
    """
    seen = set()
    l = 0
    longest = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        longest = max(longest, (r+1)-l)
        seen.add(s[r])

    return longest


def review6(s: str) -> int:
    """
    Mochi 4-18-24
    """
    seen = set()

    length = 0
    l = 0
    for r, c in enumerate(s):
        while c in seen:
            seen.remove(s[l])
            l += 1
        seen.add(c)
        length = max(r+1-l, length)

    return length


def review7(s: str) -> int:
    """
    Mochi 10-9-24
    """
    # Input: s = "pwwkew"
    # Output: 3
    count = {}
    # p: 0
    # w: 1
    result = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while max(count.values()) > 1:
            count[s[l]] -= 1
            l += 1
        result = max(result, r+1-l)

    return result


def review8(s: str) -> int:
    """
    Mochi 10-15-24
    """
    occ = set()
    res = 0

    l = 0
    for r in range(len(s)):
        while s[r] in occ:
            occ.remove(s[l])
            l += 1
        res = max(res, r+1-l)
        occ.add(s[r])
    return res
