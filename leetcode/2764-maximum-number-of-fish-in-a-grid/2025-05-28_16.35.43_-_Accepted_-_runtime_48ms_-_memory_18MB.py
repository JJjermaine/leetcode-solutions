class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.max = 0

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            total = grid[row][col]

            adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in adj:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] > 0:
                        total += dfs(new_row, new_col)

            return total

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0 and (i, j) not in visited:
                    component_sum = dfs(i, j)
                    self.max = max(self.max, component_sum)

        return self.max
                    
