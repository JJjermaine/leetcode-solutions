class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        NSmax = [0] * cols
        EWmax = [0] * rows
        for i in range(rows):
            for j in range(cols):
                NSmax[j] = max(NSmax[j], grid[i][j])
                EWmax[i] = max(EWmax[i], grid[i][j])

        res = 0
        for i in range(rows):
            for j in range(cols):
                res += abs(grid[i][j] - min(NSmax[j], EWmax[i]))
        return res