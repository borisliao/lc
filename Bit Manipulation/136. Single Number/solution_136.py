from collections import Counter, defaultdict
from typing import List


def invalid_solution(nums: List[int]) -> int:
    """
    This solution does not satisfy time and memory complexity.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    values = []
    for i in nums:  # O(n)
        if i not in values:  # in operator for list is O(n)
            values.append(i)
        else:
            values.remove(i)
    return values[0]


def ans_initial_val(nums: List[int]) -> int:
    """
    Set the ans to the initial value nums[0]
    but that's not required due to property of xor
    value b xor with 0 will equal b

    a | b | a ^ b
    --|---|------
    0 | 0 | 0 <- this property
    0 | 1 | 1 <- this property
    1 | 0 | 1
    1 | 1 | 0

    Time Complexity: O(n)
    Space Complexity: O(1) (constant extra space)
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i]

    return ans


def singleNumber(nums: List[int]) -> int:
    """
    Set the ans to the initial value 0
    due to property of xor
    value b xor with 0 will equal b

    a | b | a ^ b
    --|---|------
    0 | 0 | 0 <- this property
    0 | 1 | 1 <- this property
    1 | 0 | 1
    1 | 1 | 0

    the XOR operation is associative and commutative. That means a ^ (b ^ c) = (a ^ b) ^ c, and a ^ b = b ^ a.

    Time Complexity: O(n)
    Space Complexity: O(1) (constant extra space)
    """
    ans = 0
    for num in nums:
        ans ^= num

    return ans


def review1(nums: List[int]) -> int:
    """
    Anki 12-4-23
    Used: previous solution
    Time: 10m
    """
    ans = 0
    for n in nums:
        ans ^= n

    return ans


def review2(nums: List[int]) -> int:
    """
    Anki 12-4-23
    Does not use constant space
    Time: 1 min
    """
    n_counter = Counter(nums)

    for n, i in n_counter.items():
        if i == 1:
            return n


def review3(nums: List[int]) -> int:
    """
    Anki 12-4-23
    Does not use constant space
    Time: 1 min
    """
    n_count = defaultdict(lambda: 0)

    for n in nums:
        n_count[n] += 1
        if n_count[n] == 2:
            del (n_count[n])

    for n, i in n_count.items():
        if i == 1:
            return n
