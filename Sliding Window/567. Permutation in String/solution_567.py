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


def review9(s1: str, s2: str) -> bool:
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


def review10(s1: str, s2: str) -> bool:
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


def review11(s1: str, s2: str) -> bool:
    """
    Anki 2-6-24
    Time: 9:21
    Used: debugger 1
    """
    a = Counter(s1)
    b = Counter()
    l = 0

    for r, c in enumerate(s2):
        b[c] += 1
        if r+1-l == len(s1):
            if a == b:
                return True
            b[s2[l]] -= 1  # d1 b[l]
            l += 1
    return False


def review12(s1: str, s2: str) -> bool:
    """
    Anki 2-6-24
    Time: 12 min, 9m+3m
    """
    a = Counter(s1)
    b = Counter()
    l = 0
    matches = 0

    for r, c in enumerate(s2):
        b[c] += 1
        if b[c] == a[c]:
            matches += 1
        if r+1-l == len(s1):
            if matches == len(a):
                return True
            if b[s2[l]] == a[s2[l]]:
                matches -= 1
            b[s2[l]] -= 1  # d1 b[l]
            l += 1
    return False


def review13(s1: str, s2: str) -> bool:
    """
    Mochi 10-8-24
    """
    count = {}
    for c in s1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    window = {}
    for i, c in enumerate(s2):

        if c in window:
            window[c] += 1
        else:
            window[c] = 1

        if sum(count.values()) == sum(window.values()):  # d2
            allMatch = True
            for c in window:
                if c in count and count[c] == window[c]:
                    pass
                else:
                    allMatch = False
            if allMatch:
                return allMatch

            character = s2[i-len(count)+1]  # d1
            window[character] -= 1
            if window[character] == 0:
                del window[character]

    return False


def review14(s1: str, s2: str) -> bool:
    """
    Mochi 10-14-24
    """
    count = Counter(s1)
    window = Counter(s2[0:len(s1)])

    if count == window:
        return True

    l = 0
    for r in range(len(s1), len(s2)):
        window[s2[l]] -= 1
        l += 1
        window[s2[r]] += 1
        if count == window:
            return True
    return False


def review15(s1: str, s2: str) -> bool:
    """
    Mochi 10-15-24
    """
    compare = {}
    for s in s1:
        compare[s] = compare.get(s, 0) + 1

    window = {}
    l = 0
    for r in range(len(s2)):
        window[s2[r]] = window.get(s2[r], 0) + 1
        if r+1-l == len(s1):
            match = True
            for c in compare:
                if match == False:
                    pass
                if c not in window:
                    match = False
                elif window[c] != compare[c]:
                    match = False
            if match:
                return True
            window[s2[l]] -= 1
            l += 1
    return False
