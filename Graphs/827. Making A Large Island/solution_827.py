def largestIsland(grid: list[list[int]]) -> int:
    """
    Mochi 4-28-24
    """
    islandCount = {0: 0}  # d4 0:0

    def markIslands(r, c, id, visited: set):
        if (r, c) in visited or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
            return

        grid[r][c] = id
        islandCount[id] = 1 + islandCount.get(id, 0)
        visited.add((r, c))
        markIslands(r-1, c, id, visited)
        markIslands(r+1, c, id, visited)
        markIslands(r, c-1, id, visited)
        markIslands(r, c+1, id, visited)

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            id = -len(islandCount)-1
            if grid[r][c] == 1:
                markIslands(r, c, id, set())

    def countIslands(r, c):
        seen = set()  # d2 seen

        top = 0
        if 0 <= r-1 < len(grid) and grid[r-1][c] not in seen:
            top = islandCount[grid[r-1][c]]
            seen.add(grid[r-1][c])

        bot = 0
        if 0 <= r + 1 < len(grid) and grid[r+1][c] not in seen:
            bot = islandCount[grid[r+1][c]]
            seen.add(grid[r+1][c])

        lef = 0
        if 0 <= c - 1 < len(grid[r]) and grid[r][c-1] not in seen:
            lef = islandCount[grid[r][c-1]]
            seen.add(grid[r][c-1])

        rig = 0
        if 0 <= c + 1 < len(grid[r]) and grid[r][c+1] not in seen:
            rig = islandCount[grid[r][c+1]]

        return top + bot + lef + rig

    amountOfIslands = max(islandCount.values()) if len(
        islandCount) else 0  # d1 0, d3 if len(islandCount)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 0:
                amountOfIslands = max(
                    amountOfIslands, 1 + countIslands(r, c))

    return amountOfIslands


# def review1(grid: list[list[int]]) -> int:
#     """
#     Mochi 6-26-24
#     """
#     seen = set()

#     def get_size(r, c):
#         if (r, c) not in seen or r < 0 or c < 0 or r >= len(grid) or c >= len(grid) or grid[r][c] == 0:
#             return 0

#         seen.add((r, c))
#         return 1 + get_size(r+1, c) + get_size(r-1, c) + get_size(r, c+1) + get_size(r, c-1)

#     largest = 0

#     for r in range(len(grid)):
#         for c in range(len(grid[r])):
#             if grid[r][c] == 0:
#                 grid[r][c] == 1
#                 seen = set()
#                 largest = max(get_size(r, c), largest)
#                 grid[r][c] == 0
#             else:
#                 seen = set()
#                 largest = max(get_size(r, c), largest)

#     return largest
