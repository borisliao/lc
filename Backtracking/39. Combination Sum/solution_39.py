from typing import List


def review1(candidates: List[int], target: int) -> List[List[int]]:
    """
    Anki 12-4-23
    Time: 1h
    Used: Debugger (7)
    """
    result = []
    combination = []

    def dfs(n):
        combination.append(n)

        if sum(combination) > target:  # d4
            combination.pop()  # d1
            return
        elif sum(combination) == target:  # d4
            def same_elements(x, y):
                sorted_x = sorted(x)  # d6
                sorted_y = sorted(y)  # d6
                return sorted_x == sorted_y

            for r in result:  # d5
                if same_elements(r, combination):
                    combination.pop()  # d7
                    return

            result.append(combination.copy())  # d2
            combination.pop()  # d1, d3
            return

        for c in candidates:
            dfs(c)

        if combination:
            combination.pop()  # d5

    for c in candidates:
        dfs(c)

        if combination:
            combination.pop()  # d6

    return result


def review2(candidates: List[int], target: int) -> List[List[int]]:
    """
    12-4-23
    Used: solution (1), [Combination Sum - Backtracking - Leetcode 39 - Python](https://www.youtube.com/watch?v=GBKI9VSKdGg)
    """
    result = []
    current = []

    def dfs(i):
        if sum(current) == target:
            result.append(current.copy())
            return
        if sum(current) > target or i >= len(candidates):  # s1
            return

        current.append(candidates[i])
        dfs(i)
        current.pop()
        dfs(i+1)

    dfs(0)
    return result


def review3(candidates: List[int], target: int) -> List[List[int]]:
    """
    Anki 12-4-23
    Used: debugger (1)
    Time: 14:06
    """
    result = []
    combination = []

    def dfs(i):
        if sum(combination) == target:
            result.append(combination.copy())
            return
        if sum(combination) > target or i > len(candidates) - 1:  # d1 forgot i > len(candidates) - 1
            return

        combination.append(candidates[i])
        dfs(i)
        combination.pop()
        dfs(i+1)

    dfs(0)
    return result


def neetcode(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i: int, cur: list, total: int):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


def review4(candidates: List[int], target: int) -> List[List[int]]:
    """
    Anki 12-11-23
    Misunderstood question: "The same number may be chosen from candidates an unlimited number of times."
    Used: debugger 3, solution 1
    Time: 25:41
    """
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return
        if i >= len(candidates) or sum(subset) > target:
            return

        subset.append(candidates[i])
        dfs(i)
        subset.pop()
        dfs(i+1)

    dfs(0)  # d1, d3
    return result


def review5(candidates: List[int], target: int) -> List[List[int]]:
    """
    Anki 12-11-23
    Time: 12:12
    """
    result = []
    subset = []

    def dfs(i):
        if sum(subset) == target:
            result.append(subset.copy())
            return
        if i >= len(candidates) or sum(subset) > target:
            return

        subset.append(candidates[i])
        dfs(i)
        subset.pop()
        dfs(i+1)

    dfs(0)
    return result
