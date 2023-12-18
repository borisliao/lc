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
            l += 1

    return False


def review1(nums: List[int], target: int) -> bool:
    """
    Anki 12-15-23
    Time: 23:06
    """
    l = 0
    r = len(nums)-1

    while l <= r:
        m = (l+r)//2

        if nums[m] == target:
            return True

        side = 'unknown'  # s1

        if nums[m] > nums[l]:  # s2, nums[-1]
            side = 'left'
        elif nums[m] < nums[l]:  # s2, nums[-1]
            side = 'right'

        if side == 'left':
            if nums[0] <= target < nums[m]:
                r = m-1
            else:
                l = m + 1
        elif side == 'right':
            if nums[m] < target <= nums[-1]:
                l = m + 1
            else:
                r = m - 1
        elif side == 'unknown':  # s1
            l += 1

    return False


def review2(nums: List[int], target: int) -> bool:
    """
    Anki 12-15-23
    Time: 11 min
    Used: Solution (1)
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return True

        side = 'unknown'

        if nums[m] < nums[l]:  # s1 nums[0]
            side = 'right'
        elif nums[m] > nums[l]:  # s1 nums[0]
            side = 'left'

        if side == 'right':
            if nums[m] < target <= nums[-1]:
                l = m + 1
            else:
                r = m - 1
        elif side == 'left':
            if nums[0] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            l += 1

    return False
