import math
from typing import List


# def bruteForce(piles: List[int], h: int) -> int:
#     k = 0
#     guess = float('inf')

#     while guess <= h:
#         k+=1
#         guess = 0

#         for bananas in piles:
#             guess += bananas//k + (1 if bananas % k > 0 else 0)

#     return k

def neetcode(piles: List[int], h: int) -> int:
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


def review1(piles: List[int], h: int) -> int:
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
