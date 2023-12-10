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


def review1(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-8-23
    Time: 35:31
    Used: debugger (3)
    """
    result = []
    subset = []

    def dfs(choices: list):
        if len(subset) == len(nums):
            result.append(subset.copy())
            return

        if not choices:  # d2
            return

        for c in choices:  # d1
            subset.append(c)
            new_choice = choices.copy()  # d3
            new_choice.remove(c)  # d3
            dfs(new_choice)  # d1, d3
            subset.pop()

    dfs(nums)
    return result


def review2(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-10-23
    Used: Solution (2)
    Time: 12:09
    """
    result = []
    subset = []

    def dfs(choices: list):
        if not choices:
            result.append(subset.copy())

        for i, c in enumerate(choices):
            subset.append(c)
            new_choices = choices.copy()
            del new_choices[i]
            dfs(new_choices)
            subset.pop()

    dfs(nums)  # s2
    return result
