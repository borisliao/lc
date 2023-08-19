from typing import List


# def onlyHoriAndVert(board: List[List[str]]) -> bool:
#         vert = { i: {sudoku_num: 0 for sudoku_num in range(1,10)} for i in range(9)}
#         hori = { i: {sudoku_num: 0 for sudoku_num in range(1,10)} for i in range(9)}

#         for row in range(9):
#             for col in range(9):
#                 sudoku_num = board[row][col]
#                 if sudoku_num != '.':
#                     hori_count = hori[row][int(sudoku_num)]
#                     if(hori_count >= 1): return False 
#                     # update internal hori count
#                     hori[row][int(sudoku_num)] +=1

#                     vert_count = vert[col][int(sudoku_num)]
#                     if(vert_count >= 1): return False 
#                     # update internal veri count
#                     vert[col][int(sudoku_num)] +=1

#         return True

 
def bruteForceHashMap(board: List[List[str]]) -> bool:
    vert = { i: {sudoku_num: 0 for sudoku_num in range(1,10)} for i in range(9)}
    hori = { i: {sudoku_num: 0 for sudoku_num in range(1,10)} for i in range(9)}
    cube = { i: {sudoku_num: 0 for sudoku_num in range(1,10)} for i in range(9)}

    for row in range(9):
        for col in range(9):
            sudoku_num = board[row][col]
            if sudoku_num != '.':
                hori_count = hori[row][int(sudoku_num)]
                if(hori_count >= 1): return False 
                # update internal hori count
                hori[row][int(sudoku_num)] +=1

                vert_count = vert[col][int(sudoku_num)]
                if(vert_count >= 1): return False 
                # update internal veri count
                vert[col][int(sudoku_num)] +=1

                quad = 100
                if row < 3:
                    if col < 3:
                        quad = 0
                    elif col >= 3 and col < 6:
                        quad = 1
                    else:
                        quad = 2
                elif row >=3 and row < 6:
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
                if(cube_count >= 1): return False 
                # update internal veri count
                cube[quad][int(sudoku_num)] +=1

    return True

