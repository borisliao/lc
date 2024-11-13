from bisect import bisect_left


def search(nums: list[int], target: int) -> int:
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


def review1(nums: list[int], target: int) -> int:
    """
    Anki 11-13-23
    Used: Solution on [Youtube Comment](https://www.youtube.com/watch?v=U8XENwh8Oy8&lc=UgzE25qbCIdDk9JtL0B4AaABAg)
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


def lc_TrentonO(nums: list[int], target: int) -> int:
    """
    # [Three Lines of Python](https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/3879735/three-lines-of-python/)

    If I were writing real code, then for the sake of clarity I would (at the very least) expand the second line into an if-else block. But it's still fun to solve in as few lines as possible.

    # Complexity

    - Time complexity: O(log(n))

    - Space complexity: O(1) additional space.

    [bisect docs](https://docs.python.org/3/library/bisect.html)
    """
    rotation = bisect_left(nums[:-1], True, key=lambda n: n < nums[-1])
    idx = bisect_left(
        nums, target, **{'lo' if target <= nums[-1] else 'hi': rotation})

    return idx if nums[idx] == target else -1


def review3(nums: list[int], target: int) -> int:
    """
    Anki 11-14-23
    Used: Debugging (5), Review solution
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (r + l) // 2

        if nums[m] == target:
            return m

        side = 'right' if nums[m] < nums[-1] else 'left'

        if side == 'left':
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if side == 'right':
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def review4(nums: list[int], target: int) -> int:
    """
    Anki 11-14-23
    Used: debugger (1)
    Time: 26 min
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        side = 'right' if nums[m] < nums[0] else 'left'  # debugger (1)

        if side == 'left':
            # everything on the left side is lower.
            # we can safely check everything on the
            # left side without hitting a pivot
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if side == 'right':
            # everything on the right side is higher.
            # we can safely check everything on the
            # right side without hitting a pivot
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def review5(nums: list[int], target: int) -> int:
    """
    Anki 11-14-23
    Used: debugger (2), peek solution (1)
    Time: 20 min
    """
    l = 0
    r = len(nums) - 1  # debugger (1)

    while l <= r:  # peek solution (1)
        m = (l + r) // 2  # int overflow safe version is m = r + (l-r)//2;

        if nums[m] == target:
            return m

        side = 'right' if nums[m] < nums[-1] else 'left'  # debugger (2)

        if side == 'left':
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if side == 'right':
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def review6(nums: list[int], target: int) -> int:
    """
    Anki 11-19-23
    Used: debugger (1)
    Time: 6m46s
    """
    l = 0
    r = len(nums) - 1

    while l <= r:  # debugger (1)
        m = (l + r) // 2

        if nums[m] == target:
            return m

        side = 'right' if nums[m] < nums[-1] else 'left'  # ex. 3 4 5 1 2

        if side == 'left':
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if side == 'right':
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def review7(nums: list[int], target: int) -> int:
    """
    Anki 11-29-23
    Used: debugger (1)
    Time: 9:32
    """
    l = 0
    r = len(nums) - 1  # 1d

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        side = 'right' if nums[m] < nums[-1] else 'left'

        if side == 'right':
            # everything on the right side is higher.
            # we can safely check everything on the
            # right side without hitting a pivot
            if nums[m] < target <= nums[-1]:
                l = m + 1
            else:
                r = m - 1

        if side == 'left':
            # everything on the left side is lower.
            # we can safely check everything on the
            # left side without hitting a pivot
            if nums[0] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

    return -1


def review8(nums: list[int], target: int) -> int:
    """
    Anki 12-22-23
    Time: 18:33
    Used: Debugger 1
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return m

        # d1 < edge case [3,1]
        side = 'left' if nums[l] <= nums[m] else 'right'

        if side == 'left':
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def review9(nums: list[int], target: int) -> int:
    """
    Mochi 4-8-23
    Time: 5 min
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def review10(nums: list[int], target: int) -> int:
    """
    Mochi 10-22-24
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:  # left side
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:  # right side
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def review11(nums: list[int], target: int) -> int:
    """
    Mochi 11-10-24
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def review12(nums: list[int], target: int) -> int:
    """
    Mochi 11-11-24
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l+r)//2

        if nums[m] == target:
            return m

        if nums[m] <= nums[r]:
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
