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
