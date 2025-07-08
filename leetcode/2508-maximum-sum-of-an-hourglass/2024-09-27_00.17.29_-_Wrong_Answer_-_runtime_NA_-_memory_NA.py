class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                # top, middle, and bottom
                top = grid[row][col] + grid[row][col+1] + grid[row][col+2]
                middle = grid[row+1][col+1]
                bottom = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
                max_sum = max((top + middle + bottom), max_sum)

        return max_sum
        