def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 4-17-24
    """
    l = 0
    r = len(matrix) - 1

    while l <= r:
        m = (l+r) // 2
        if target < matrix[m][0]:
            r = m - 1
        elif matrix[m][-1] < target:
            l = m + 1
        else:
            break

    for row in range(l, r+1):
        i = 0
        j = len(matrix[row]) - 1

        while i <= j:
            m = (i+j) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                i = m + 1
            elif target < matrix[row][m]:
                j = m - 1
    return False
