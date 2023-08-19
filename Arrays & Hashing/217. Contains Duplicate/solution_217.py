from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False


def naive(nums: List[int]) -> bool:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1) (no memory needed)
    """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Sorting Solution
# def sorting(nums: List[int]) -> bool:
#     pass


# Hash Set Solution
# def hashset(nums: List[int]) -> bool:
#     pass
