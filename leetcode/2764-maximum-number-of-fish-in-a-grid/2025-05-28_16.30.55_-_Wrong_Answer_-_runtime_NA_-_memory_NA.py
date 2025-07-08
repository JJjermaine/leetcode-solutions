class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.max = 0

        def dfs(row, col, value):
            visited.add((row, col))
            self.max = max(value, self.max)

            adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for z in adj:
                i, j = z
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] > 0 and (new_row, new_col) not in visited:
                        grid[new_row][new_col] += value
                        dfs(new_row, new_col, grid[new_row][new_col])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0 and (i, j) not in visited:
                    dfs(i, j, grid[i][j])

        return self.max
                
