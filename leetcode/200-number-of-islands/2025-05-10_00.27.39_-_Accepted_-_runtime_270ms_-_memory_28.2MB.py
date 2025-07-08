class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])        
        def in_bounds(row, col):
            return 0 <= row < n and 0 <= col < m

        seen = set()
        res = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j):
            seen.add((i, j))
            for r, c in directions:
                if not in_bounds(i+r, j+c):
                    continue
                if grid[i+r][j+c] == "1" and grid[i+r][j+c] == "1" and (i+r, j+c) not in seen:
                    dfs(i+r, j+c)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in seen:
                    res += 1  # new island found
                    dfs(i, j)
        return res