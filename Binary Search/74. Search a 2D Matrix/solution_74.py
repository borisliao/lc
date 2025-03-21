def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    l, r = 0, len(matrix) - 1

    while l <= r:
        if matrix[l][0] < target and matrix[l][len(matrix[0]) - 1] < target:
            l += 1
        elif matrix[r][0] > target and matrix[r][len(matrix[0]) - 1] > target:
            r -= 1
        else:
            i = l
            l, r = 0, len(matrix[i]) - 1

            while l <= r:
                if matrix[i][l] < target:
                    l += 1
                elif matrix[i][r] > target:
                    r -= 1
                else:
                    return True

            return False

    return False


def review1(matrix: list[list[int]], target: int) -> bool:
    """
    Anki 11-19-23
    Used: debugger (1)
    Time: 14m17s
    """
    l = 0
    r = len(matrix) - 1

    row_with_target = None

    while l <= r:
        m = (l + r) // 2
        if matrix[m][0] <= target <= matrix[m][-1]:
            row_with_target = m
            break

        if matrix[m][0] < target:
            l += 1
        else:
            r -= 1

    if row_with_target == None:  # debugger (1)
        return False

    l = 0
    r = len(matrix[row_with_target])

    while l <= r:
        m = (l + r) // 2
        if matrix[row_with_target][m] == target:
            return True

        if matrix[row_with_target][m] < target:
            l += 1
        else:
            r -= 1

    return False


def review2(matrix: list[list[int]], target: int) -> bool:
    """
    Anki 11-27-23
    Time: 27:28
    """
    l = 0
    r = len(matrix) - 1
    target_row = None
    while l <= r:
        m = (r + l) // 2
        if matrix[m][0] <= target <= matrix[m][-1]:
            target_row = m
            break

        if target > matrix[m][-1]:
            l += 1
        else:
            r -= 1

    if target_row == None:
        return False

    l = 0
    r = len(matrix[target_row]) - 1

    while l <= r:
        m = (r+l) // 2
        if matrix[target_row][m] == target:
            return True

        if matrix[target_row][m] < target:
            l += 1
        else:
            r -= 1

    return False


def review3(matrix: list[list[int]], target: int) -> bool:
    """
    Anki 12-21-23
    Time: 18:13
    Used: Debugger 1
    """
    l = 0
    r = len(matrix)

    row = None
    while l <= r:
        m = (l+r) // 2

        if matrix[m][0] <= target <= matrix[m][-1]:
            row = m
            break

        if matrix[m][-1] < target:
            l += 1
        else:
            r -= 1

    if row == None:
        return False

    l = 0
    r = len(matrix[row])

    while l <= r:
        m = (l+r)//2
        if matrix[row][m] == target:  # d1 matrix[m]
            return True

        if matrix[row][m] > target:  # d1 matrix[m]
            r = m - 1
        else:
            l = m + 1

    return False


def review4(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 4-17-24
    Time: 11:13
    """
    l = 0
    r = len(matrix) - 1
    row = None

    while l <= r:
        m = (l + r) // 2
        if matrix[m][0] <= target <= matrix[m][-1]:
            row = m
            break
        if target < matrix[m][0]:
            r = m - 1
        else:
            l = m + 1

    result = False
    if row != None:  # d1 != None
        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                result = True
                break
            if matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1

    return result


def review5(matrix: list[list[int]], target: int) -> bool:
    """
    Mochi 11-17-24
    """
    l, r = 0, len(matrix) - 1

    row = None
    while l <= r and not row:
        m = (l+r) // 2
        if matrix[m][0] <= target <= matrix[m][-1]:
            row = matrix[m]
        elif matrix[m][-1] < target:
            l = m + 1
        else:
            r = m - 1

    if not row:
        return False

    l, r = 0, len(row) - 1

    while l <= r:
        m = (l+r) // 2
        if row[m] == target:
            return True
        elif row[m] < target:
            l = m + 1
        else:
            r = m - 1

    return False
