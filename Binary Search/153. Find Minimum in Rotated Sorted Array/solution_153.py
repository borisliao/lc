from typing import List


def neetCode(nums: List[int]) -> int:
    """
    https://www.youtube.com/watch?v=nIVW4P8b1VA
    """
    l, r = 0, len(nums) - 1

    lowest = nums[0]
    while l <= r:
        if nums[l] <= nums[r]:
            return nums[l]

        m = (l + r) // 2

        lowest = min(nums[m], lowest)
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    return lowest


def youtubeCommentOptimization(nums: List[int]) -> int:
    """
    https://www.youtube.com/watch?v=nIVW4P8b1VA&lc=UgwpyIcgEwwDVzN735d4AaABAg
    """
    l, r = 0, len(nums) - 1

    lowest = nums[0]
    while l <= r:
        m = (l + r) // 2

        lowest = min(nums[m], lowest)
        if nums[m] <= nums[r]:
            r = m - 1
        else:
            l = m + 1

    return lowest
