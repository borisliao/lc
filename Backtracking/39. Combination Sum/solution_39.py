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
