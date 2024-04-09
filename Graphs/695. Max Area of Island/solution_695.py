from collections import deque


def maxAreaOfIsland(grid: list[list[int]]) -> int:
    q = deque()
    area = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                q.append((r, c))

            q_area = 0
            while q:
                i, j = q.popleft()
                # d1 j < len(grid)
                if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == 1:
                    grid[i][j] = 0
                    q_area += 1
                    q.append((i-1, j))
                    q.append((i+1, j))
                    q.append((i, j-1))
                    q.append((i, j+1))
            area = max(area, q_area)

    return area


def review1(grid: list[list[int]]) -> int:
    """
    Mochi 4-8-24
    Time: 15 min
    """
    def fill(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + fill(r-1, c) + fill(r+1, c) + fill(r, c-1) + fill(r, c+1)

    island_size = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                amount = fill(r, c)
                island_size = max(amount, island_size)

    return island_size
