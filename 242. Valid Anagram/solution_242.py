def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    for letter in t:
        if letter not in s:
            return False
        
    return True