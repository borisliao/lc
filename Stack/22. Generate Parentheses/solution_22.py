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
    Time: 17 min
    """
    stack = []
    result = []

    def dfs(open, close):
        if open == close == n:
            result.append("".join(stack))
            return
        if open < n:
            stack.append('(')
            dfs(open+1, close)
            stack.pop()
        if open > close:
            stack.append(')')
            dfs(open, close + 1)
            stack.pop()

    dfs(0, 0)
    return result


def review2(n: int) -> list[str]:
    """
    Anki 1-16-24
    Used: solution 1
    """
    result = []
    stack = []

    def dfs(open, close):
        if open == close == n:  # s1 == 3
            result.append(''.join(stack))
            return
        if open < n:
            stack.append('(')
            dfs(open+1, close)
            stack.pop()
        if open > close:  # s1
            stack.append(')')
            dfs(open, close+1)
            stack.pop()

    dfs(0, 0)
    return result


def review3(n: int) -> list[str]:
    """
    Anki 1-16-24
    Time: 6 min
    """
    stack = []
    result = []

    def dfs(open, close):
        if open == close == n:
            result.append(''.join(stack))
            return
        if open < n:
            stack.append('(')
            dfs(open+1, close)
            stack.pop()
        if close < open:
            stack.append(')')
            dfs(open, close+1)
            stack.pop()

    dfs(0, 0)
    return result


def review4(n: int) -> list[str]:
    """
    Anki 1-18-24
    Time: 2:43
    """
    result = []
    subset = []

    def dfs(open, close):
        if open == close == n:
            result.append(''.join(subset))
            return
        if open < n:
            subset.append('(')
            dfs(open+1, close)
            subset.pop()
        if close < open:
            subset.append(')')
            dfs(open, close+1)
            subset.pop()
    dfs(0, 0)
    return result


def review5(n: int) -> list[str]:
    """
    Anki 1-26-24
    Time: 8 min
    Used: debugger 1
    """
    result = []
    subset = []

    def dfs(open, close):
        if n == open == close:
            result.append(''.join(subset))
            return
        if open < n:
            subset.append('(')
            dfs(open+1, close)
            subset.pop()
        if close < open:  # d1 close > open
            subset.append(')')
            dfs(open, close+1)
            subset.pop()
    dfs(0, 0)
    return result


def review6(n: int) -> list[str]:
    """
    Anki 2-5-24
    Time: 3:35
    """
    result = []
    subset = []

    def dfs(open, close):
        if open == close == n:
            result.append(''.join(subset))
            return
        if open < n:
            subset.append('(')
            dfs(open+1, close)
            subset.pop()
        if close < open:
            subset.append(')')
            dfs(open, close+1)
            subset.pop()
    dfs(0, 0)
    return result


def review7(n: int) -> list[str]:
    """
    Mochi 4-16-24
    """
    result = []
    subset = []

    def dfs(open, close):
        if open == close == n:
            result.append(''.join(subset))
            return
        if open < n:
            subset.append('(')
            dfs(open+1, close)
            subset.pop()
        if open > close:
            subset.append(')')
            dfs(open, close+1)
            subset.pop()
    dfs(0, 0)
    return result


def review8(n: int) -> list[str]:
    """
    Mochi 10-6-24
    """
    res = []
    stack = ''

    def dfs(open, close):
        nonlocal stack
        if open == close == n:
            res.append(stack)
            return  # d1
        if open < n:
            stack += '('
            dfs(open+1, close)
            stack = stack[:-1]  # d1

        if close < n and open > close:
            stack += ')'
            dfs(open, close+1)
            stack = stack[:-1]  # d1

    dfs(0, 0)
    return res
