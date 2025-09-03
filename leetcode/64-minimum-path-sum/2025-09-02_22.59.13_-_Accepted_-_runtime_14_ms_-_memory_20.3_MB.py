class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0: # skip first
                    continue
                elif i == 0: # if first row, look at left only
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0: # if first col, look at top only
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else: # else choose either left or top
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]