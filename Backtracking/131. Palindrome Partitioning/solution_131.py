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


def review1(s: str) -> list[list[str]]:
    """
    Anki 12-13-23
    Used: Debugger 2
    Time: 11:55
    """
    result = []
    subset = [s[0]]  # d2

    def dfs(i):
        if i == len(s):
            if subset:
                for substring in subset:
                    if substring != substring[::-1]:
                        return
                result.append(subset.copy())
            return

        subset[-1] += s[i]  # d1
        dfs(i+1)
        subset[-1] = subset[-1][:-1]
        subset.append(s[i])
        dfs(i+1)
        subset.pop()

    dfs(1)  # d2
    return result


def review2(s: str) -> list[list[str]]:
    """
    Anki 12-18-23
    Time: 8:57
    Used: solution 1, debugger 1
    Original solution O(2^n)
    """
    result = []
    subset = [s[0]]  # s1 'a' instead of s[0]

    def dfs(i):
        if i >= len(s):
            for word in subset:  # d2 used s instead of word
                if word != word[::-1]:  # d2 s collision with global s
                    return
            result.append(subset.copy())
            return

        subset.append(s[i])
        dfs(i+1)
        subset.pop()
        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]

    dfs(1)
    return result


def review3(s: str) -> list[list[str]]:
    """
    12-18-23
    Neetcode solution O(n^n)
    Time: 26:53
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(s):
            result.append(subset.copy())
            return

        for j in range(i, len(s)):  # s1 range(i+1,len(s))
            word = s[i:j+1]  # s1 s[i:j]
            if word != word[::-1]:
                continue
            subset.append(s[i:j+1])  # s1 s[i:j]
            dfs(j+1)  # s2 i+1
            subset.pop()

    dfs(0)
    return result


def review4(s: str) -> list[list[str]]:
    """
    Anki 1-1-24
    """
    result = []
    subset = [s[0]]

    def dfs(i):
        if i == len(s):  # s2 swapped
            for word in subset:  # s3
                if word != word[::-1]:  # s3
                    return  # s3
            result.append(subset.copy())
            return

        subset.append(s[i])
        dfs(i+1)
        subset.pop()  # s3
        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]  # d1 subset instead of subset[-1]

    dfs(1)
    return result


def review5(s: str) -> list[list[str]]:
    """
    Anki 1-1-24
    Time: 10 min
    """
    result = []
    subset = [s[0]]

    def dfs(i):
        if i >= len(s):
            for word in subset:
                if word != word[::-1]:
                    return
            result.append(subset.copy())
            return

        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]  # s1 [::-1]

        subset.append(s[i])
        dfs(i+1)
        subset.pop()

    dfs(1)
    return result


def review6(s: str) -> list[list[str]]:
    """
    Anki 1-3-24
    Used: debugger 3
    Time: 23 min
    """
    result = []
    subset = [s[0]]

    def dfs(i):
        if i >= len(s):  # d2 >
            for word in subset:  # d3
                if word != word[::-1]:  # d3
                    return  # d3
            result.append(subset.copy())
            return

        subset.append(s[i])
        dfs(i+1)
        subset.pop()

        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]

    dfs(1)  # d1
    return result


def review7(s: str) -> list[list[str]]:
    """
    1-3-24
    """
    result = []
    subset = [s[0]]

    def dfs(i):
        if i >= len(s):
            if subset[-1] != subset[-1][::-1]:
                return
            result.append(subset.copy())
            return

        if subset[-1] == subset[-1][::-1]:
            subset.append(s[i])
            dfs(i+1)
            subset.pop()

        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]

    dfs(1)
    return result


def review8(s: str) -> list[list[str]]:
    """
    Anki 1-12-24
    Time: 20 min
    """
    subset = [s[0]]  # d3 []
    result = []

    def dfs(i):
        if i >= len(s):
            if subset[-1] != subset[-1][::-1]:  # d1
                return  # d1
            result.append(subset.copy())
            return

        subset[-1] += s[i]
        dfs(i+1)
        subset[-1] = subset[-1][:-1]
        if subset[-1] != subset[-1][::-1]:
            return
        subset.append(s[i])
        dfs(i+1)
        subset.pop()

    dfs(1)  # d3 0
    return result


# def review9(s: str) -> list[list[str]]:
#     """
#     Anki 1-24-24
#     NOTE: Use `for j in range(i, len(s)):` and `def isPali(l, r):`
#     """
#     def isPali(l: int, r: int):
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True

#     subset = []
#     result = []

#     def dfs(i):
#         if i >= len(s):
#             result.append(subset.copy())
#             return  # d2
#         subset.append(s[i])
#         dfs(i+1)
#         subset.pop()

#         for j in range(i, len(s)):
#             if isPali(i, j):
#                 subset.append(s[i:j+1])
#                 dfs(j+1)  # d1 tab >, s3 dfs(i)
#                 subset.pop()  # d1 tab >

#     dfs(0)
#     return result


def review10(s: str) -> list[list[str]]:
    """
    Anki 1-24-24
    NOTE: Use `for j in range(i, len(s)):` and `def isPali(l, r):`
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(s):
            result.append(subset.copy())
            return
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                subset.append(s[i:j+1])
                dfs(j+1)
                subset.pop()
    dfs(0)
    return result


def review11(s: str) -> list[list[str]]:
    """
    Anki 1-26-24
    NOTE: Use `for j in range(i, len(s)):` and `def isPali(l, r):`
    Time: 7 min
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(s):
            result.append(subset.copy())
            return
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                subset.append(s[i:j+1])
                dfs(j+1)
                subset.pop()

    dfs(0)
    return result


def review12(s: str) -> list[list[str]]:
    """
    Anki 2-5-24
    Time: 13:50
    Used: Solution 2
    """
    result = []
    subset = []

    def dfs(i):
        if i >= len(s):
            result.append(subset.copy())
            return
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:  # s1[::-1]
                subset.append(s[i:j+1])
                dfs(j+1)  # s2 +1
                subset.pop()
    dfs(0)
    return result
