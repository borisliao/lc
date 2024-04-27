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


def review1(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 4-19-24
    """
    l = 0
    r = len(matrix) - 1

    while l < r:
        if matrix[r][0] > target:
            r -= 1
        elif matrix[l][-1] < target:
            l += 1
        else:
            break

    for row in range(l, r+1):
        i, j = 0, len(matrix[row]) - 1

        while i <= j:
            m = (i+j)//2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                i += 1
            else:
                j -= 1
    return False


def review2(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 4-24-24
    """

    for r in range(len(matrix)):
        i = 0
        j = len(matrix[r]) - 1

        while i <= j:
            m = (i+j) // 2
            if matrix[r][m] < target:
                i = m + 1
            elif matrix[r][m] > target:
                j = m - 1
            else:
                return True
    return False


def review3(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 4-27-24
    Time: 12:18
    """
    l = 0
    r = len(matrix) - 1

    while l <= r:
        m = (l + r)//2
        if matrix[m][0] > target:
            r = m - 1
        elif matrix[m][0] < target:
            l = m + 1
        else:
            return True

    intersection = l
    for i in range(intersection):
        l = 0
        r = len(matrix[i]) - 1

        while l <= r:
            m = (l+r)//2
            if matrix[i][m] == target:
                return True
            if matrix[i][m] < target:
                l = m + 1
            else:
                r = m - 1
    return False
