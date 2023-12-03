from typing import List


def neetcode(nums: List[int]) -> List[List[int]]:
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


def review1(nums: List[int]) -> List[List[int]]:
    """
    Anki 1-3-23
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
