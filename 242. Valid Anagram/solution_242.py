# def naive(s: str, t: str) -> bool:
#     if len(s) != len(t): return False

#     for letter in t:
#         if letter not in s:
#             return False
        
#     return True

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

