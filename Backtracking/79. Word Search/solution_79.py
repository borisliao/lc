# def exist(board: list[list[str]], word: str) -> bool:
#     w = ['']
#     visited = set()

#     def dfs(i, j):
#         w[0] += board[i][j]
#         visited.add((i, j))  # d4

#         if len(w[0]) > len(word) or word[len(w[0]) - 1] != w[0][len(w[0]) - 1] or (i, j) in visited:  # d2, d3, d4, d5
#             w[0] = w[0][:-1]
#             visited.remove((i, j))  # d5
#             return False

#         if w[0] == word:
#             return True

#         if i - 1 > 0:
#             if dfs(i - 1, j):
#                 return True
#         if i + 1 < len(board) - 1:
#             if dfs(i + 1, j):
#                 return True
#         if j - 1 < 0:
#             if dfs(i, j - 1):
#                 return True
#         if j + 1 < len(board[i]) - 1:
#             if dfs(i, j + 1):
#                 return True

#     for i in range(len(board)):  # d1
#         for j in range(len(board[i])):  # d1
#             if dfs(i, j):
#                 return True

#     return False

from collections import Counter, defaultdict


def neetcode(board: list[list[str]], word: str) -> bool:
    """
    https://www.youtube.com/watch?v=pfiQ_PS1g8E
    O(n * m * 4^n)
    """
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (
            min(r, c) < 0
            or r >= ROWS
            or c >= COLS
            or word[i] != board[r][c]
            or (r, c) in path
        ):
            return False
        path.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return res

    # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
    count = defaultdict(int, sum(map(Counter, board), Counter()))

    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False


def review1(board: list[list[str]], word: str) -> bool:
    """
    Anki 12-8-23
    Time: 34:56
    Used: debugger (3), solution (1)
    """
    visited = set()

    def dfs(r, c, i):
        if (i >= len(word) or
                r < 0 or r >= len(board) or
                c < 0 or c >= len(board[r]) or
                word[i] != board[r][c] or
                (r, c) in visited):
            return False

        if i == len(word) - 1:  # s2
            return True

        visited.add((r, c))
        result = (dfs(r-1, c, i+1) or
                  dfs(r+1, c, i+1) or
                  dfs(r, c-1, i+1) or
                  dfs(r, c+1, i+1))
        visited.remove((r, c))  # d1
        return result

    for r in range(len(board)):  # d3
        for c in range(len(board[r])):  # d3
            if dfs(r, c, 0):  # d3, d4
                return True  # d3

    return False  # d3


# def review2(board: list[list[str]], word: str) -> bool:
#     """
#     Anki 12-8-23
#     """
#     subset = ['']
#     visited = set()  # s1

#     def dfs(i, j):
#         if subset[0] == word:
#             return True
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or (i, j) in visited:
#             subset[0] = subset[0][:-1]
#             return False
#         if board[i][j] == word[len(subset[0])-1]:
#             subset[0] += word[len(subset[0])-1]
#             visited.add((i, j))  # s1
#         else:
#             return False

#         return dfs(i-1, j) or dfs(i+1, j) or dfs(i, j-1) or dfs(i+1, j-1)

#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if dfs(i, j):
#                 return True

#     return False

def review3(board: list[list[str]], word: str) -> bool:
    """
    Anki 12-18-23
    Time: 33:06
    Used: solution 6, debugger 1
    """
    visited = set()

    def dfs(r, c, i):
        # s3 replaced subset=[''] with i check and len(word) instead of len(board)
        if i == len(word):  # s7 len(word)-1 instead of len(word)
            return True

        if ((r, c) in visited or
                r < 0 or c < 0 or
                r >= len(board) or
                c >= len(board[r]) or
                word[i] != board[r][c] or  # s6
                i >= len(word)):  # s4
            return False

        visited.add((r, c))
        has_word = (dfs(r-1, c, i+1) or
                    dfs(r+1, c, i+1) or
                    dfs(r, c-1, i+1) or  # d2 ',' instead of 'or'
                    dfs(r, c+1, i+1))
        visited.remove((r, c))
        return has_word  # s5 removed visited before returning

    for r in range(len(board)):  # s1 should itterate through the board
        for c in range(len(board[r])):
            found_word = dfs(r, c, 0)
            if found_word:
                return True
    return False


def review4(board: list[list[str]], word: str) -> bool:
    """
    Anki 12-21-23
    Time: 38:46
    Used: Debugger 3
    """
    visited = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or
            r >= len(board) or
            c >= len(board[r]) or  # d2 r >=
            board[r][c] != word[i] or
                (r, c) in visited):  # d3 visited
            return False

        visited.add((r, c))
        has_character = (dfs(r-1, c, i+1) or
                         dfs(r+1, c, i+1) or
                         dfs(r, c-1, i+1) or
                         dfs(r, c+1, i+1))
        visited.remove((r, c))
        return has_character

    for r in range(len(board)):  # d1 range(len
        for c in range(len(board[r])):  # d1 range(len
            if dfs(r, c, 0):
                return True

    return False


def review5(board: list[list[str]], word: str) -> bool:
    """
    Anki 12-31-23
    Time: 10 min
    """
    visited = set()

    def dfs(r, c, i):
        if i >= len(word):
            return True

        if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]) or board[r][c] != word[i] or (r, c) in visited:
            return False

        visited.add((r, c))
        return dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)

    for r in range(len(board)):
        for c in range(len(board[r])):
            if dfs(r, c, 0):
                return True

    return False
