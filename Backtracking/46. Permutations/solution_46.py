def permute(nums: list[int]) -> list[list[int]]:
    """
    12-4-23
    Time: 12:41
    """
    result = []
    permutation = []

    def dfs(n: list):
        if len(permutation) == len(nums):
            result.append(permutation.copy())
            return

        for i, num in enumerate(n):
            permutation.append(num)
            new_n = n.copy()
            del new_n[i]
            dfs(new_n)
            permutation.pop()

    dfs(nums)
    return result


def neetcode(nums: list[int]) -> list[list[int]]:
    """[Backtracking: Permutations - Leetcode 46 - Python](https://www.youtube.com/watch?v=s7AvT7cGdSo)"""
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = neetcode(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res
