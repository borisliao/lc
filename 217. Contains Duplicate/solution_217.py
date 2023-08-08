from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
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
