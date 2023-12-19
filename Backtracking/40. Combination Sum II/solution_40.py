# def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
#     """
#     12-5-23
#     """
#     result = set()
#     combination = []

#     def dfs(i):
#         if sum(combination) == target:
#             result.add(tuple(sorted(combination)))  # d2
#             return
#         if i > len(candidates) - 1 or sum(combination) > target:
#             return

#         combination.append(candidates[i])
#         dfs(i+1)
#         combination.pop()
#         dfs(i+1)

#     dfs(0)  # d1
#     return [list(x) for x in result]

def review1(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 12-5-23
    Used: solution (3)
    Time: 11:27
    """
    candidates.sort()

    result = []
    canidate = []

    def dfs(i):
        if sum(canidate) == target:
            result.append(canidate.copy())
            return
        if i > len(candidates) - 1 or sum(canidate) > target:
            return

        canidate.append(candidates[i])
        dfs(i+1)
        canidate.pop()
        # s1, s2, s3
        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i+1)

    dfs(0)
    return result


def neetcode(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()

    res = []

    def backtrack(cur, pos, target):
        if target == 0:
            res.append(cur.copy())
            return
        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res


def review2(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 12-7-23
    Time: 7:11
    """
    candidates.sort()

    result = []
    combination = []

    def dfs(i):
        if sum(combination) == target:
            result.append(combination.copy())
            return

        if i > len(candidates) - 1 or sum(combination) > target:
            return

        combination.append(candidates[i])
        dfs(i+1)
        combination.pop()
        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i+1)

    dfs(0)
    return result


def review3(candidates: list[int], target: int) -> list[list[int]]:
    """
    12-7-23
    Uses passed param and copy macro
    """
    candidates.sort()
    result = []

    def dfs(i: int, combination: list):
        if sum(combination) == target:
            result.append(combination[::])
            return

        if i > len(candidates) - 1 or sum(combination) > target:
            return

        combination.append(candidates[i])
        dfs(i+1, combination)
        combination.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i+1, combination)

    dfs(0, [])
    return result


def review4(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 12-7-23
    Used: Solution (3)
    Time: 16:38
    """
    candidates.sort()
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return

        if i >= len(candidates) or sum(subset) > target:  # s1
            return

        subset.append(candidates[i])
        dfs(i+1)
        subset.pop()
        # s2, s3
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        dfs(i+1)

    dfs(0)
    return result


def review5(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 12-18-23
    Used: solution 4
    Time: 24:33
    """
    candidates.sort()

    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return

        if i >= len(candidates) or sum(subset) > target:  # s1 forgot i >= len(candidates)
            return

        subset.append(candidates[i])
        dfs(i+1)  # s4 dfs(i)
        value = subset.pop()
        # s2 forgot i + 1 < len(candidates), s3 candidates[i] == candidates[i+1], i4 check i+1 not i itself
        while i + 1 < len(candidates) and candidates[i+1] == value:
            i += 1
        dfs(i+1)  # s4 dfs(i)

    dfs(0)
    return result
