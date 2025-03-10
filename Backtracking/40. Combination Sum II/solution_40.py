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


def review6(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 12-25-23
    Time: 9:58
    Used: solution 1, debugger 1
    """
    candidates.sort()
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())  # d2 .copy()
            return
        if i >= len(candidates) or sum(subset) > target:  # s1 forgot i >= len(candidates)
            return

        subset.append(candidates[i])
        dfs(i+1)
        subset.pop()
        while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
            i += 1
        dfs(i+1)

    dfs(0)
    return result


def review7(candidates: list[int], target: int) -> list[list[int]]:
    """
    Anki 1-28-24
    Time: 12 min
    Used: Solution 1
    """
    candidates.sort()
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return
        if sum(subset) > target or i >= len(candidates):
            return

        subset.append(candidates[i])
        i += 1
        dfs(i)  # s1
        subset.pop()  # s1
        while i < len(candidates) and candidates[i-1] == candidates[i]:
            i += 1
        dfs(i)

    dfs(0)
    return result


def review8(candidates: list[int], target: int) -> list[list[int]]:
    """
    Mochi 4-15-24
    Time: 27:32
    """
    candidates.sort()
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return

        if sum(subset) > target or i >= len(candidates):
            return

        subset.append(candidates[i])
        i += 1
        dfs(i)  # s1
        subset.pop()  # s1
        while i < len(candidates) and candidates[i-1] == candidates[i]:
            i += 1
        dfs(i)

    dfs(0)
    return result


def review9(candidates: list[int], target: int) -> list[list[int]]:
    """
    Mochi 11-6-24
    """
    candidates.sort()

    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return
        if i >= len(candidates) or sum(subset) > target:
            return
        subset.append(candidates[i])
        dfs(i+1)
        subset.pop()
        j = i + 1
        while j < len(candidates) and candidates[j-1] == candidates[j]:
            j += 1
        dfs(j)

    dfs(0)
    return result
