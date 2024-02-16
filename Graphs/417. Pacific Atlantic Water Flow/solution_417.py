def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    pacific = set()
    alantic = set()
    result = []

    def dfs(r, c, l, s, visited):
        # s1 or heights[r][c] < l
        if (r, c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[r]) or heights[r][c] < l:
            return

        visited.add((r, c))
        if l <= heights[r][c]:
            s.add((r, c))
        else:  # s1
            return  # s1

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
