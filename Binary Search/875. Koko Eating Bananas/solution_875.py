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
