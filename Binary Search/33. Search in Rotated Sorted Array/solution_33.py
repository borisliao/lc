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


def review1(nums: List[int], target: int) -> bool:
    """
    Anki 11-13-23
    Used: Solution on [Youtube Comment](https://www.youtube.com/channel/UCark0s3kcaj3T05U7iy1Z1w)
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        # left sorted portion
        elif nums[mid] >= nums[l]:
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # right sorted portion
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


def review2(nums: List[int], target: int) -> bool:
    """
    Review
    Use 2 binary searches to find the pivot
    """
    pass
