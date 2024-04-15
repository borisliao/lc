def neetCode(nums: list[int]) -> int:
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


def youtubeCommentOptimization(nums: list[int]) -> int:
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


def review1(nums: list[int]) -> int:
    """
    Anki 11-20-23
    Used: debugger (2) (for edge cases)
    Time: 37m02s, whiteboard
    """
    l = 0
    r = len(nums) - 1

    if len(nums) == 1:  # debugger (1)
        return nums[0]

    while l <= r:
        m = (l + r) // 2

        side = 'right' if nums[m] <= nums[-1] else 'left'  # debugger (2)

        if side is 'left':
            l = m + 1

        if side is 'right':
            r = m - 1

    return nums[r + 1]


def review2(nums: list[int]) -> int:
    """
    Anki 12-20-23
    Time: 17:11
    Used: Debugger 1
    """
    l = 0
    r = len(nums) - 1
    minimum = float('inf')

    while l <= r:
        m = (l+r) // 2

        minimum = min(minimum, nums[m])
        # d1 nums[m] > nums[l]
        side = 'right' if nums[m] <= nums[r] else 'left'

        if side == 'left':
            l = m + 1
        else:
            r = m - 1

    return minimum


def review3(nums: list[int]) -> int:
    """
    Mochi 4-15-24
    Time: 16:53, 3:53
    """
    l = 0
    r = len(nums)-1
    smallest = float('inf')

    while l <= r:
        m = (l+r) // 2

        smallest = min(smallest, nums[m])
        if nums[m] < nums[r]:
            r = m - 1
        else:
            l = m + 1

    return smallest
