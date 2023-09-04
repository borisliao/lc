from typing import List


def neetCode(nums: List[int], target: int) -> bool:
    """
    daily leetcode problem on august 9.
    https://www.youtube.com/watch?v=oUnF7o88_Xc
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return True

        if nums[l] < nums[m]:
            # on the left side
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        elif nums[l] > nums[m]:
            # on the right side
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

        else:
            l+=1

    return False
