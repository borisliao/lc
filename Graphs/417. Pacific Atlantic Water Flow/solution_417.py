def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    pacific = set()
    alantic = set()
    result = []

    def dfs(r, c, l, s, visited):
        # s1 or heights[r][c] < l
        if (r, c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[r]) or heights[r][c] < l:
            return

        visited.add((r, c))
        s.add((r, c))

        dfs(r-1, c, max(l, heights[r][c]), s, visited)
        dfs(r+1, c, max(l, heights[r][c]), s, visited)
        dfs(r, c-1, max(l, heights[r][c]), s, visited)
        dfs(r, c+1, max(l, heights[r][c]), s, visited)

    r = len(heights)
    c = len(heights[r-1])
    for i in range(c):
        dfs(0, i, 0, pacific, set())
        dfs(r-1, i, 0, alantic, set())

    for i in range(r):
        dfs(i, 0, 0, pacific, set())
        dfs(i, c-1, 0, alantic, set())

    for i, j in pacific:
        if (i, j) in alantic:
            result.append([i, j])

    return result


def review1(heights: list[list[int]]) -> list[list[int]]:
    """
    Mochi 4-15-24
    Time: 46:55
    """
    visited_pacific = set()
    visited_alantic = set()

    def find_inc(r, c, val, alantic=False):
        if not alantic:
            visited = visited_pacific
        else:
            visited = visited_alantic

        if (r, c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[r]) or heights[r][c] < val:
            return

        visited.add((r, c))
        find_inc(r+1, c, heights[r][c], alantic)
        find_inc(r-1, c, heights[r][c], alantic)
        find_inc(r, c+1, heights[r][c], alantic)
        find_inc(r, c-1, heights[r][c], alantic)

    ROW = len(heights)
    COL = len(heights[0])
    # Pacific
    for r in range(ROW):
        find_inc(r, 0, 0, alantic=False)
    for c in range(COL):
        find_inc(0, c, 0, alantic=False)

    # Alantic
    for r in range(ROW):
        find_inc(r, COL-1, 0, alantic=True)
    for c in range(COL):
        find_inc(ROW-1, c, 0, alantic=True)
    matches = []
    for r in range(ROW):
        for c in range(COL):
            if (r, c) in visited_alantic and (r, c) in visited_pacific:
                matches.append([r, c])
    return matches


def lc_darkTianTian(matrix: list[list[int]]) -> list[list[int]]:
    """https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/264494/python-very-concise-solution-using-dfs-set-128ms"""
    if not matrix:
        return []
    p_land = set()
    a_land = set()
    R, C = len(matrix), len(matrix[0])

    def spread(i, j, land):
        land.add((i, j))
        for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
            if (0 <= x < R and 0 <= y < C and matrix[x][y] >= matrix[i][j]
                    and (x, y) not in land):
                spread(x, y, land)

    for i in range(R):
        spread(i, 0, p_land)
        spread(i, C-1, a_land)
    for j in range(C):
        spread(0, j, p_land)
        spread(R-1, j, a_land)
    return list(p_land & a_land)
