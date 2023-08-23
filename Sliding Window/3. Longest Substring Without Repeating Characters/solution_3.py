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
            L+=1
    
        seen.add(s[r])

        length = max(len(seen), length)
    
    return length
