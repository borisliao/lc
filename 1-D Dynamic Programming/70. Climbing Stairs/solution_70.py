def climbStairs(n: int) -> int:
    """
    12-22-23
    Time: 12:42
    Added Memoization
    """
    returns = {}

    def dfs(s):
        if s == 0:
            return 1
        if s < 0:
            return 0

        if s in returns:
            return returns[s]

        returns[s-1] = dfs(s-1)
        returns[s-2] = dfs(s-2)
        return returns[s-1] + returns[s-2]

    return dfs(n)


def review1(n: int) -> int:
    """
    Anki 12-29-23
    Time: 30 min
    Used: debugger
    """
    cache = {}  # d1 add memoization

    def dfs(i):
        if i > n:
            return 0
        elif i == n:
            return 1
        else:
            i1 = None  # d1 add memoization
            if i+1 in cache:  # d1 add memoization
                i1 = cache[i+1]  # d1 add memoization
            else:
                i1 = dfs(i+1)  # d1 add memoization
                cache[i+1] = i1  # d1 add memoization
            i2 = None  # d1 add memoization
            if i+2 in cache:  # d1 add memoization
                i2 = cache[i+2]  # d1 add memoization
            else:
                i2 = dfs(i+2)  # d1 add memoization
                cache[i+2] = i2  # d1 add memoization
            return i1 + i2  # d1 add memoization

    return dfs(0)


def review4(n: int) -> int:
    """
    Anki 12-31-23
    Time: 20 min
    Used: [Climbing Stairs - Dynamic Programming - Leetcode 70 - Python](https://www.youtube.com/watch?v=Y0lT9Fck7qI)
    """
    one, two = 1, 1

    for _ in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


def review5(n: int) -> int:
    """
    Anki 1-1-24
    Time: 4 min
    Used: debugger 1
    """
    one, two = 1, 0

    for _ in range(n):  # d1 len(n)
        one, two = one + two, one

    return one


def review5(n: int) -> int:
    """
    Anki 1-1-24
    Time: 6 min
    Used: Debugger 1
    """
    one, two = 0, 1

    for _ in range(n):
        one, two = two, one + two  # d1 two, one

    return two


def review6(n: int) -> int:
    """
    Anki 2-3-24
    Time: 16:23
    Used: Debugger 1
    """
    # 1       |             1
    # 2 1     |             2
    # 3 2 1   |             4
    # 4 3 2 1 | 2 + 2 + 4 = 6

    l = 1
    r = 0

    for _ in range(n):  # d1 len(n)
        l, r = l + r, l

    return l  # d1 r


def review7(n: int) -> int:
    """
    Mochi 4-15-24
    """
    one, two = 1, 0

    for _ in range(n):
        one, two = one+two, one

    return one


def review8(n: int) -> int:
    """
    Mochi 10-3-24
    """
    result = 0
    subset = []

    def dfs():
        if sum(subset) > n:
            return

        if sum(subset) == n:
            nonlocal result

            result += 1
            return

        subset.append(1)
        dfs()
        subset.pop()
        subset.append(2)
        dfs()
        subset.pop()

    dfs()
    return result
