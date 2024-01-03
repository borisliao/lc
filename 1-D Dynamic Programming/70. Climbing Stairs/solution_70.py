# def climbStairs(n: int) -> int:
#     """
#     12-22-23
#     Time: 7:21
#     Brute force
#     """
#     result = [0]

#     def dfs(steps_left):
#         if steps_left == 0:
#             result[0] += 1
#             return
#         if steps_left < 0:
#             return

#         dfs(steps_left-1)
#         dfs(steps_left-2)

#     dfs(n)
#     return result[0]

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


# def review3(n: int) -> int:
#     """
#     Anki 12-29-23
#     Used: solution, [Amazon Coding Interview Question - Recursive Staircase Problem](https://www.youtube.com/watch?v=5o-kdjv7FD0)
#     Brute force solution, same as climbStairs()
#     """
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return review3(n-1) + review3(n-2)


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
