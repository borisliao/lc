def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    """
    12-5-23
    Used: solution (4), debugger (1)
    [Subsets II - Backtracking - Leetcode 90 - Python](https://www.youtube.com/watch?v=Vn2v6ajA7U0)
    Time: 42:27
    """
    result = []
    subset = []
    nums.sort()  # s1

    def dfs(i):
        if i == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)  # s2
        subset.pop()
        while len(nums)-1 > i and nums[i] == nums[i+1]:  # s3, s4
            i += 1
        dfs(i + 1)

    dfs(0)  # d5
    return result


def setAsResult(nums: list[int]) -> list[list[int]]:
    """
    12-5-23
    Used: solution (4), debugger (1)
    [Youtube Comment](https://www.youtube.com/watch?v=Vn2v6ajA7U0&lc=UgzXIybvTfdMkxwUdlx4AaABAg)
    """
    result = set()
    subset = []
    nums.sort()  # s1

    def dfs(i):
        if i == len(nums):
            result.add(tuple(subset.copy()))
            return

        subset.append(nums[i])
        dfs(i + 1)  # s2
        subset.pop()
        dfs(i + 1)

    dfs(0)  # d5
    return [list(x) for x in result]


def review1(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-10-23
    Time: 28:08
    Used: Debugger (3)
    """
    nums.sort()

    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            return

        subset.append(nums[i])
        result.append(subset.copy())
        prev_p = None

        for p in range(i + 1, len(nums)):
            if nums[p] == prev_p:  # d1 nums[p]
                continue
            prev_p = nums[p]  # d1 nums[p]
            dfs(p)
            subset.pop()

    result.append([])

    prev_i = None  # d2
    for i in range(len(nums)):
        if nums[i] == prev_i:  # d3 nums[i]
            continue
        dfs(i)
        prev_i = subset.pop()  # d2

    return result


def review2(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-18-23
    Time: 18:16
    Used: Debugger 1
    """
    nums.sort()

    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)
        value = subset.pop()
        while i+1 < len(nums) and nums[i+1] == value:  # d1 nums[i+1] != value
            i += 1
        dfs(i+1)

    dfs(0)
    return result
