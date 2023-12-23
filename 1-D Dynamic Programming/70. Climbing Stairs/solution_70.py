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
