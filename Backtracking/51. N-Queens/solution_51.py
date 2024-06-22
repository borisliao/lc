# def solveNQueens(n: int) -> list[list[str]]:
#     result = []
#     subset = [['.' for _ in range(n)] for _ in range(n)]
#     q_row, q_col, q_left, q_right = set(), set(), set(), set()

#     def is_valid(r, c):
#         if r in q_row or c in q_col:
#             return False
#         # q_left is vertical col

#         # q_right is vertical row


def neetcode(n: int) -> list[list[str]]:
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res
