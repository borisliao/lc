import math


def neetcode(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l+r)//2
        kHours = 0

        for p in piles:
            kHours += math.ceil(p/k)

        if kHours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


def review1(piles: list[int], h: int) -> int:
    """
    Anki 11-29-23
    Used: Hint (binary search section, optimal solution o(nlogn)), solution
    Time: 1:03:01
    """
    l = 1
    r = max(piles)
    result = r

    while l <= r:
        m = (l + r) // 2
        hours_to_finish = sum([math.ceil(p/m) for p in piles])
        if hours_to_finish > h:
            l = m + 1
        else:
            result = min(result, m)
            r = m - 1

    return result


def review2(piles: list[int], h: int) -> int:
    """
    Anki 11-30-23
    Used: debugger (2)
    Time: 20:43
    """
    l = 1  # d1 (needs to be 0, not min(piles) because we are trying to find the minimum k, not just a valid k pile), d2 (needs to be 1 because 0 will always fail)
    r = max(piles)
    lowest_k = r

    while l <= r:
        k = (l + r) // 2
        hours = sum([math.ceil(p/k) for p in piles])
        if hours > h:
            l = k + 1
        else:
            lowest_k = min(lowest_k, k)
            r = k - 1

    return lowest_k


def review3(piles: list[int], h: int) -> int:
    """
    Anki 12-4-23
    Time: 16:36
    """
    l = 1
    r = max(piles)

    result = None

    while l <= r:
        k = (l+r)//2

        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours <= h:
            result = k
            r = k - 1
        else:
            l = k + 1

    return result


def review4(piles: list[int], h: int) -> int:
    """
    Anki 12-20-23
    Used: Solution 5
    Time: 29:12
    """
    l = 1  # s5 (needs to be 1 because 0 will always fail)
    r = max(piles)
    minK = r  # s4 minK = 0

    while l <= r:
        k = (l+r) // 2

        hours = sum([math.ceil(p/k) for p in piles])

        if hours > h:
            l = k + 1  # s2 l+=1
        elif hours <= h:
            minK = min(minK, k)  # s1 put in wrong if statement, s3 maxK
            r = k - 1  # s2 r+=1

    return minK


def review5(piles: list[int], h: int) -> int:
    """
    Anki 12-20-23
    Time: 7 min
    Used: debugger 1
    """
    l = 1  # d1 should not search 0
    r = max(piles)

    minimum_k = r

    while l <= r:
        k = (l+r) // 2
        hours = sum([math.ceil(p/k) for p in piles])

        if hours <= h:
            minimum_k = min(minimum_k, k)
            r = k - 1
        else:
            l = k + 1

    return minimum_k


def review6(piles: list[int], h: int) -> int:
    """
    Anki 12-22-23
    Time: 18:32
    """
    l = 1
    r = max(piles)
    minK = r

    while l <= r:
        k = (l+r) // 2

        hours = sum([math.ceil(p/k) for p in piles])

        if hours > h:
            l = k + 1
        else:
            minK = min(k, minK)
            r = k - 1

    return minK


def review7(piles: list[int], h: int) -> int:
    """
    Anki 12-31-23
    Used: Debugger 4
    Time: 12 min
    Read question carefully next time...
    """
    l = 1  # d3 0
    r = max(piles)
    smallest_k = r  # d2 largest_k
    while l <= r:
        k = (l+r)//2
        hours = sum([math.ceil(p/k) for p in piles])

        if hours > h:  # d1 >=
            l = k + 1  # d4 statement flipped
        else:
            smallest_k = min(smallest_k, k)  # d2 largest_k
            r = k - 1  # d4 statement flipped

    return smallest_k  # d2 largest_k


def review8(piles: list[int], h: int) -> int:
    """
    Anki 1-21-24
    Time: 5 min
    Used: Debugger 1
    """
    l = 1  # d1 0
    r = max(piles)
    minK = r

    while l <= r:
        k = (l+r)//2
        hours = sum([math.ceil(p/k) for p in piles])

        if hours <= h:
            minK = min(minK, k)
            r = k - 1
        else:
            l = k + 1

    return minK


def review9(piles: list[int], h: int) -> int:
    """
    Mochi 4-18-24
    Time: 11:23
    """
    min_k = float('inf')
    l = 1  # d1 0
    r = max(piles)

    while l <= r:
        k = (l+r)//2
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        if hours <= h:
            min_k = min(min_k, k)
            r = k - 1
        else:
            l = k + 1

    return min_k


def review10(piles: list[int], h: int) -> int:
    """
    Mochi 10-23-24
    """
    l = 1  # d1 0
    r = max(piles)
    res = r
    while l <= r:
        k = (l+r)//2
        if sum([math.ceil(p/k) for p in piles]) > h:
            l = k + 1
        else:
            res = min(res, k)
            r = k - 1

    return res
