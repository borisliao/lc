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


# def review1(nums: List[int]) -> List[List[int]]:
#     """
#     """
#     pass
