from collections import defaultdict
from typing import List


def bruteForceHashMap(board: List[List[str]]) -> bool:
    vert = {i: {sudoku_num: 0 for sudoku_num in range(
        1, 10)} for i in range(9)}
    hori = {i: {sudoku_num: 0 for sudoku_num in range(
        1, 10)} for i in range(9)}
    cube = {i: {sudoku_num: 0 for sudoku_num in range(
        1, 10)} for i in range(9)}

    for row in range(9):
        for col in range(9):
            sudoku_num = board[row][col]
            if sudoku_num != '.':
                hori_count = hori[row][int(sudoku_num)]
                if (hori_count >= 1):
                    return False
                # update internal hori count
                hori[row][int(sudoku_num)] += 1

                vert_count = vert[col][int(sudoku_num)]
                if (vert_count >= 1):
                    return False
                # update internal veri count
                vert[col][int(sudoku_num)] += 1

                quad = 100
                if row < 3:
                    if col < 3:
                        quad = 0
                    elif col >= 3 and col < 6:
                        quad = 1
                    else:
                        quad = 2
                elif row >= 3 and row < 6:
                    if col < 3:
                        quad = 3
                    elif col >= 3 and col < 6:
                        quad = 4
                    else:
                        quad = 5
                else:
                    if col < 3:
                        quad = 6
                    elif col >= 3 and col < 6:
                        quad = 7
                    else:
                        quad = 8

                cube_count = cube[quad][int(sudoku_num)]
                if (cube_count >= 1):
                    return False
                # update internal veri count
                cube[quad][int(sudoku_num)] += 1

    return True


def review1(board: List[List[str]]) -> bool:
    """
    Neetcode soluton
    https://www.youtube.com/watch?v=TjFXEUCMqI8
    Anki review 10/16/23

    Use a hashmap with the corresponding key to look up if the number already exists
    """
    row = defaultdict(set)  # length of 9 (rows)
    col = defaultdict(set)  # length of 9 (cols)
    cube = defaultdict(set)  # length of 9 (cubes)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if board[r][c] in row[r]:
                return False
            if board[r][c] in col[c]:
                return False
            if board[r][c] in cube[(r//3, c//3)]:
                return False

            row[r].add(board[r][c])
            col[c].add(board[r][c])
            cube[(r//3, c//3)].add(board[r][c])

    return True


def review2(board: List[List[str]]) -> bool:
    """Anki Reviewed 10/29/23"""
    row = defaultdict(set)
    col = defaultdict(set)
    box = defaultdict(set)

    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == ".":
                continue
            if c in row[i]:
                return False
            if c in col[j]:
                return False
            if c in box[(i//3, j//3)]:
                return False

            row[i].add(c)
            col[j].add(c)
            box[(i//3, j//3)].add(c)

    return True


def review3(board: List[List[str]]) -> bool:
    """
    Anki 11-27-23
    Used: debugger (1)
    Time: 28:55
    """

    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    sqr = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':  # 1d
                continue
            if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in sqr[i//3][j//3]:
                return False
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            sqr[i//3][j//3].add(board[i][j])

    return True


def review4(board: List[List[str]]) -> bool:
    """
    Anki 12-29-23
    Time: 30 min
    Used: debugger 4, solution 1
    """
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    sqr = {(i//3, i % 3): set() for i in range(9)}

    for r in range(9):  # s4 3
        for c in range(9):  # s4 3
            if board[r][c] == '.':  # d4
                continue  # d4
            # d5 sqr[(r, c)]
            if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sqr[(r//3, c//3)]:
                return False
            row[r].add(board[r][c])  # d1 .add
            col[c].add(board[r][c])  # d1 .add
            # d1 .add, i2 //, d3 board[r][c]
            sqr[(r // 3, c // 3)].add(board[r][c])

    return True


def review5(board: list[list[str]]) -> bool:
    """
    Anki 2-13-24
    Time: 8:43
    """
    row = defaultdict(lambda: set())
    col = defaultdict(lambda: set())
    sqr = defaultdict(lambda: set())

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            if num in row[r] or num in col[c] or num in sqr[(r//3, c//3)]:
                return False
            row[r].add(board[r][c])
            col[c].add(board[r][c])
            sqr[(r//3, c//3)].add(board[r][c])

    return True


def review6(board: list[list[str]]) -> bool:
    hori = {r: set() for r in range(len(board))}
    verti = {c: set() for c in range(len(board))}
    cubic = {}
    for r in range(3):
        for c in range(3):
            cubic[(r, c)] = set()

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == '.':
                pass
            elif board[r][c] in hori[r] or board[r][c] in verti[c] or board[r][c] in cubic[(r//3, c//3)]:
                return False
            else:
                hori[r].add(board[r][c])
                verti[c].add(board[r][c])
                cubic[(r//3, c//3)].add(board[r][c])

    return True
