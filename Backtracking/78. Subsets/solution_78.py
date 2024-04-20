def neetcode(nums: list[int]) -> list[list[int]]:
    """ https://www.youtube.com/watch?v=REOH22Xwdkk """
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


def review1(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-3-23
    Used: Peak at solution (2)
    Time: 13:50
    [The Backtracking Blueprint: The Legendary 3 Keys To Backtracking Algorithms](https://www.youtube.com/watch?v=Zq4upTEaQyM)
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())  # s2, need to copy
            return  # s1, did not return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result


def review2(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-3-23
    Used: [Subsets - Backtracking - Leetcode 78](https://www.youtube.com/watch?v=REOH22Xwdkk), solution (2)
    Time: 8:48
    This is a binary decision tree to include or exclude
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())  # s2
            return

        subset.append(nums[i])
        dfs(i+1)

        # traverse in right part of decision tree
        subset.pop()
        dfs(i+1)

    dfs(0)  # s1
    return result


def review3(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-9-23
    Used: debugger (2)
    Time: 30 min
    This decision tree traverses through all nums itterations
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            return

        subset.append(nums[i])
        result.append(subset.copy())

        for n in range(i + 1, len(nums)):  # d1
            dfs(n)
            subset.pop()

    result.append([])  # d2

    for n in range(len(nums)):
        dfs(n)
        subset.pop()

    return result


def review4(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-18-23
    Time: 1:59
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return result


def review5(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-17-24
    Time: 7 min
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return result


def review6(nums: list[int]) -> list[list[int]]:
    """
    Mochi 4-20-24
    Time: 2 min
    """
    result = []
    subset = []

    def dfs(i):
        if i == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return result
