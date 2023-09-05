from typing import List


def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[m] < nums[l]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

    return -1
