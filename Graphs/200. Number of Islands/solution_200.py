def numIslands(grid: list[list[str]]) -> int:
    """
    1-31-24
    Time: 14:25
    Used: Debugger 1
    """
    islands = 0

    def setTo0(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        setTo0(r-1, c)
        setTo0(r+1, c)
        setTo0(r, c-1)
        setTo0(r, c+1)

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':  # d1 == 1 (int)
                islands += 1
                setTo0(r, c)

    return islands


def review1(grid: list[list[str]]) -> int:
    """
    Anki 2-6-24
    Time: 12 min
    Used: debugger 1
    """
    def markIsland(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        markIsland(r-1, c)
        markIsland(r+1, c)
        markIsland(r, c-1)
        markIsland(r, c+1)

    islands = 0
    for r in range(len(grid)):  # d1
        for c in range(len(grid[r])):  # d1
            if grid[r][c] == '1':
                islands += 1
                markIsland(r, c)

    return islands


def review2(grid: list[list[str]]) -> int:
    """
    Mochi 4-14-24
    dfs
    """
    def fill(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        fill(r+1, c)
        fill(r-1, c)
        fill(r, c-1)
        fill(r, c+1)

    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                islands += 1
                fill(r, c)

    return islands


def review3(grid: list[list[str]]) -> int:
    """
    4-14-24
    bfs
    """
    def fill(i, j):
        q = [(i, j)]
        while q:
            newQ = []
            for r, c in q:
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != '1':
                    continue
                grid[r][c] = '0'
                newQ.append((r+1, c))
                newQ.append((r-1, c))
                newQ.append((r, c-1))
                newQ.append((r, c+1))
            q = newQ

    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                islands += 1
                fill(r, c)

    return islands
