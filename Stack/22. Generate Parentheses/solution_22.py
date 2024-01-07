def generateParenthesis(n: int) -> list[str]:
    """
    Anki 1-6-24
    Time: 55 min
    Used: [Generate Parentheses - Stack - Leetcode 22](https://www.youtube.com/watch?v=s9fokUqJ76A)
    """
    result = []
    subset = []

    def dfs(i, j):
        if i == j == n:
            result.append(''.join(subset))
            return
        if i < n:
            subset.append('(')
            dfs(i+1, j)
            subset.pop()  # s1 only did one pop after all if statements
        if j < i:  # s1 s1 j < n
            subset.append(')')
            dfs(i, j+1)
            subset.pop()  # s1

    dfs(0, 0)
    return result


def review1(n: int) -> list[str]:
    """
    Anki 1-7-24
    """
    pass
