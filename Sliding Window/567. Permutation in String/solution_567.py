from collections import Counter


def naive(s1: str, s2: str) -> bool:
    S1 = {}

    if len(s1) > len(s2):
        return False

    for char in s1:
        S1[char] = 1 + S1.get(char, 0)

    L = 0
    R = len(s1) - 1

    while R < len(s2):
        testS1 = S1.copy()
        for i in range(L, R+1):
            if s2[i] in testS1:
                testS1[s2[i]] -= 1

        # make sure testS1 values == 0
        if sum([abs(val) for val in testS1.values()]) == 0:
            return True

        L += 1
        R += 1

    return False


def review1(s1: str, s2: str) -> bool:
    """
    Anki 12-22-23
    Time: 21:19
    Used: [Permutation in String - Leetcode 567 - Python](https://www.youtube.com/watch?v=UbyhOgBN834)
    """
    l = 0
    r = len(s1)

    count1 = Counter(s1)

    while r <= len(s2):
        count2 = Counter(s2[l:r])
        if count1 == count2:
            return True
        l += 1
        r += 1
    return False
