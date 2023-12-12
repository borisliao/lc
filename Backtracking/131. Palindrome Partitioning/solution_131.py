def partition(s: str) -> list[list[str]]:
    """
    12-12-23
    Time: 55:37
    Used: debugger 6, solution 1
    """
    result = []
    subset = [s[0]]

    def dfs(i):
        if i == len(s):  # d3
            for l in subset:  # d1, d7 removed s6 optimization
                if l != l[::-1]:  # d1
                    return
            result.append(subset.copy())
            return  # d2

        if subset == []:
            subset.append(s[i])
        else:
            subset[-1] += s[i]

        dfs(i+1)
        subset[-1] = subset[-1][:-1]
        if subset[-1] == '':  # d4
            del subset[-1]  # d4
        subset.append(s[i])
        dfs(i+1)
        subset.pop()

    dfs(1)  # d5
    return result


def neetcode(s: str) -> list[list[str]]:
    """
    [Palindrome Partitioning - Backtracking - Leetcode 131](https://www.youtube.com/watch?v=3jvWodd7ht0)
    """
    def isPali(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i: j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res
