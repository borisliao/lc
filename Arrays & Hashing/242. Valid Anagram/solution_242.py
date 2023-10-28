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
            dictS[char] +=1
        else:
            dictS[char] = 1
    
    for char in t:
        if char in dictS:
            if dictS[char] == 1:
                del dictS[char]
            else:
                dictS[char] -=1
    
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