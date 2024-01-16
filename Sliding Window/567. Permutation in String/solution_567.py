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


def review2(s1: str, s2: str) -> bool:
    """
    Anki 12-22-23
    Time: 4 min
    Used: Debugger 1
    """
    c1 = {}
    for s in s1:
        c1[s] = c1.get(s, 0) + 1

    l = 0
    r = len(s1)

    while r <= len(s2):
        c2 = {}
        for s in s2[l:r]:  # d1 for s in s2:
            c2[s] = c2.get(s, 0) + 1

        if c1 == c2:
            return True
        l += 1
        r += 1
    return False


# def review3(s1: str, s2: str) -> bool:
#     """
#     Anki 12-22-23
#     Time: 30 min
#     """
#     l = 0
#     r = len(s1) - 1

#     c1 = Counter(s1)
#     c2 = Counter(s2[l:r+1])
#     match = 26
#     for s, c in c1.items():  # d1 values
#         if s not in c2:
#             match -= 1
#         else:
#             match -= abs(c2[s] - c)

#     while r < len(s2):
#         if match == 26:
#             return True

#         if s2[r] in c1:
#             match += 1
#         else:
#             match -= 1
#         r += 1  # d2

#         if s2[l] in c1:
#             match += 1
#         else:
#             match -= 1
#         l += 1

#     return False


def review3(s1: str, s2: str) -> bool:
    """
    Anki 12-22-23
    Time: 3 min
    Brute force solution
    """
    c1 = Counter(s1)
    l = 0
    r = len(s1)

    while r <= len(s2):
        c2 = Counter(s2[l:r])
        if c1 == c2:
            return True
        l += 1
        r += 1

    return False


def review4(s1: str, s2: str) -> bool:
    """
    12-22-23
    Used: https://leetcode.com/problems/permutation-in-string/solutions/3138544/python-3-7-lines-counters-w-explanation-example-t-m-64-97
    O(26 * N)
    """
    c1 = Counter(s1)
    l = 0
    r = len(s1)
    c2 = Counter(s2[l:r])

    if c1 == c2:
        return True

    while r < len(s2):
        c2[s2[l]] -= 1
        c2[s2[r]] += 1

        l += 1
        r += 1

        if c1 == c2:
            return True

    return False


def leetcode_artod(s1: str, s2: str) -> bool:
    """
    12-22-23
    https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained
    """
    cntr, w = Counter(s1), len(s1)

    for i in range(len(s2)):
        if s2[i] in cntr:
            cntr[s2[i]] -= 1
        if i >= w and s2[i-w] in cntr:
            cntr[s2[i-w]] += 1

        if all([cntr[i] == 0 for i in cntr]):  # see optimized code below
            return True

    return False


def leetcode_artod_optimized(s1: str, s2: str) -> bool:
    """
    12-22-23
    https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained
    """
    cntr, w, match = Counter(s1), len(s1), 0

    for i in range(len(s2)):
        if s2[i] in cntr:
            if not cntr[s2[i]]:
                match -= 1
            cntr[s2[i]] -= 1
            if not cntr[s2[i]]:
                match += 1

        if i >= w and s2[i-w] in cntr:
            if not cntr[s2[i-w]]:
                match -= 1
            cntr[s2[i-w]] += 1
            if not cntr[s2[i-w]]:
                match += 1

        if match == len(cntr):
            return True

    return False


def review5(s1: str, s2: str) -> bool:
    """
    Anki 12-23-23
    Time: 20 min
    O(26 * n)
    """
    c1 = Counter(s1)
    c2 = Counter(s2[0:len(s1)])
    l = 0

    if c1 == c2:
        return True

    for r in range(len(s1), len(s2)):
        c2[s2[l]] -= 1
        l += 1

        c2[s2[r]] += 1

        if c1 == c2:
            return True

    return False


def review6(s1: str, s2: str) -> bool:
    """
    Anki 12-23-23
    Time: 20 min
    O(26 * n)
    """
    c1 = Counter(s1)
    c2 = Counter(s2[0:len(s1)])
    l = 0

    if c1 == c2:
        return True

    for r in range(len(s1), len(s2)):
        c2[s2[l]] -= 1
        l += 1

        c2[s2[r]] += 1

        if c1 == c2:
            return True

    return False


# def review7(s1: str, s2: str) -> bool:
#     """
#     12-23-23
#     """
#     c1 = Counter(s1)
#     c2 = Counter(s2[0:len(s1)])

#     differences = 0
#     for character, occurances in c2.items():
#         if character in c1 and c1[character] == occurances:
#             break
#         else:
#             differences += abs(c1[character]-occurances)
#     l = 0

#     if differences == 0:
#         return True

#     for r in range(len(s1), len(s2)):

#         if c1[l] == c2[l]:
#             differences -= 1
#         elif c1[l] - 1 == c2[l]:
#             differences += 1
#         l += 1

#         if c1[r] == c2[r]:
#             differences -= 1
#         elif c1[r] + 1 == c2[r]:
#             differences += 1

#         if differences == 0:
#             return True

#     return False


def review8(s1: str, s2: str) -> bool:
    """
    Anki 12-28-23
    Time: 8 min
    """
    c1 = {}
    for c in s1:
        if c in c1:
            c1[c] += 1
        else:
            c1[c] = 1

    r = len(s1)

    while r <= len(s2):
        c2 = {}
        for c in s2[r-len(s1):r]:
            if c in c2:
                c2[c] += 1
            else:
                c2[c] = 1

        if c1 == c2:
            return True

        r += 1

    return False


# def review9(s1: str, s2: str) -> bool:
#     """
#     12-28-23
#     Time: 40 min
#     """
#     non_matches = 0

#     c1 = Counter(s1)
#     c2 = Counter(s2[0:len(s1)])  # d1
#     for c in c1:
#         non_matches += abs(c1[c] - c2[c])

#     l = 0
#     r = len(s1) - 1  # d2 - 1

#     while r < len(s2) - 1:  # d2 <=, d3 - 1
#         if non_matches == 0:
#             return True

#         if s2[l] in c1:  # d2 s1
#             non_matches -= 1
#         l += 1

#         r += 1
#         if s2[r] in c1:  # d2 s1
#             non_matches -= 1
#         else:
#             non_matches += 1

#     return False

def review8(s1: str, s2: str) -> bool:
    """
    Anki 1-16-24
    Time: 7 min
    """
    s1_count = Counter(s1)

    for r in range(len(s1), len(s2)+1):
        l = r-len(s1)
        s2_count = Counter(s2[l:r])
        if s1_count == s2_count:
            return True
    return False


def review9(s1: str, s2: str) -> bool:
    """
    Anki 1-16-24
    Time: 17 min
    """
    s1_count = Counter(s1)
    s2_count = Counter(s2[0:len(s1)])

    if s1_count == s2_count:
        return True

    for r in range(len(s1)+1, len(s2)+1):  # d1 len(s2)+1
        l = r-len(s1)
        s2_count[s2[l-1]] -= 1
        s2_count[s2[r-1]] += 1  # d1 r-1

        if s1_count == s2_count:
            return True

    return False


# def review10(s1: str, s2: str) -> bool:
#     """
#     Anki 1-16-24
#     """
