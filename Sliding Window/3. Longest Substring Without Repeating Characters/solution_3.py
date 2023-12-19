# def dictHashMap(s: str) -> int:
# # does not work for edge case for test 291
#     seenChar = {}
#     runningLength = 0
#     length = 0
#     ignore_index = -1

#     for i, char in enumerate(s):
#         if char in seenChar:
#             if ignore_index < seenChar[char]:
#                 runningLength -= seenChar[char]+1
#                 ignore_index = seenChar[char]

#             if runningLength < -1:
#                 runningLength = -1

#         runningLength += 1
#         if runningLength > length:
#             length = runningLength

#         seenChar[char] = i

#     return length

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
