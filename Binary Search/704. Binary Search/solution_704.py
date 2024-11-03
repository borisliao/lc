def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
            r -= 1
        elif nums[m] < target:
            l += 1
        else:
            return m

    return -1


def review1(nums: list[int], target: int) -> int:
    """
    Review 11-27-23
    Time: 6:05
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if target == nums[m]:
            return m

        if target < nums[m]:
            r -= 1
        else:
            l += 1

    return -1


def review2(nums: list[int], target: int) -> int:
    """
    Anki 11-27-23
    Time: 3:12
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


def review3(nums: list[int], target: int) -> int:
    """
    Anki 12-22-23
    Time: 3:16
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l += 1
        else:
            r -= 1

    return -1


def review4(nums: list[int], target: int) -> int:
    """
    Mochi 4-13-24
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l+r)//2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1


def review5(nums: list[int], target: int) -> int:
    """
    Mochi 11-3-24
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1
