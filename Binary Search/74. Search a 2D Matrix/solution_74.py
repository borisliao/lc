from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    l, r = 0, len(matrix) - 1

    while l <= r:
        if matrix[l][0] < target and matrix[l][len(matrix[0]) - 1] < target:
            l+=1
        elif matrix[r][0] > target and matrix[r][len(matrix[0]) - 1] > target:
            r-=1
        else:
            i=l
            l, r = 0, len(matrix[i]) - 1

            while l <= r:
                if matrix[i][l] < target:
                    l+=1
                elif matrix[i][r] > target:
                    r-=1
                else:
                    return True

            return False
        
    return False