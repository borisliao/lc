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


def singleNumber(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1) (constant extra space)
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i]

    return ans
