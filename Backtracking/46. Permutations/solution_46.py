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
    """
    [Backtracking: Permutations - Leetcode 46 - Python](https://www.youtube.com/watch?v=s7AvT7cGdSo)
    Note: This solution is not particularly good
    """
    res = []

    # base case
    if len(nums) == 1:
        return [nums.copy()]

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = neetcode(nums)

        for perm in perms:
            perm.append(n)
        res += perms
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


def review3(nums: list[int]) -> list[list[int]]:
    """
    Anki 12-18-23
    Used: Solution 1
    Time: 10:13
    """
    result = []
    subset = []

    def dfs(values: list):
        if len(values) == 0:
            result.append(subset.copy())
            return

        for i in range(len(values)):
            subset.append(values[i])

            new_values = values.copy()
            del new_values[i]

            dfs(new_values)

            subset.pop()  # s1

    dfs(nums)
    return result


def review4(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-1-24
    Time: 30 min
    Used: [solution comment](https://www.youtube.com/watch?v=s7AvT7cGdSo&lc=UgxL_-PwA_fneENImIp4AaABAg)
    ### [@danielsun716](https://www.youtube.com/channel/UC6YblD-4Xfux7SFTscc9Hlw) [1 year ago](https://www.youtube.com/watch?v=s7AvT7cGdSo&lc=UgxL_-PwA_fneENImIp4AaABAg)
    My thought is initially the same with Neetcode. I draw a decision tree from an empty list. So I write this code for a straight forward understanding. 
    ```
    def permute(self, nums: list:[int]) -> list[list[int]]:
        res = []
        def backtrack(nums, perm):
            if not nums:
                res.append(perm)
                return
            for i in range(len(nums)):
                backtrack(nums[: i] + nums[i + 1:], perm + [nums[i]])
        backtrack(nums, [])
        return res
    ```
    """
    result = []
    subset = []

    def dfs(options: list):
        if len(subset) == len(nums):  # d2 <
            result.append(subset.copy())
            return

        for i in range(len(options)):
            subset.append(options[i])  # s1
            dfs(options[:i] + options[i+1:])  # s1
            subset.pop()

    dfs(nums)
    return result


def review5(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-1-24
    Time: 8 min
    """
    result = []
    subset = []

    def dfs(n: list):
        if len(n) <= 0:
            result.append(subset.copy())
            return

        for i, val in enumerate(n):
            new_list = n.copy()
            subset.append(val)
            del new_list[i]
            dfs(new_list)
            subset.pop()

    dfs(nums)
    return result


def review5(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-3-24
    Time: 7 min
    """
    result = []
    subset = []

    def dfs(values):
        if len(values) == 0:
            result.append(subset.copy())
            return

        for i, v in enumerate(values):
            new_values = values.copy()
            subset.append(v)
            del new_values[i]
            dfs(new_values)
            subset.pop()

    dfs(nums)
    return result


def review6(nums: list[int]) -> list[list[int]]:
    """
    Anki 1-14-24
    Time: 6 min
    """
    result = []
    subset = []

    def dfs(choices: list):
        if len(choices) == 0:
            result.append(subset.copy())
            return

        for i in range(len(choices)):
            subset.append(choices[i])
            new_choices = choices.copy()
            del new_choices[i]
            dfs(new_choices)
            subset.pop()

    dfs(nums)
    return result


def review7(nums: list[int]) -> list[list[int]]:
    """
    Mochi 4-14-24
    Time: 5 min
    """
    result = []
    subset = []

    def dfs(vals: list):
        if not vals:
            result.append(subset.copy())
            return

        for i, n in enumerate(vals):
            subset.append(n)
            new_vals = vals.copy()
            new_vals.pop(i)
            dfs(new_vals)
            subset.pop()  # s1

    dfs(nums)
    return result
