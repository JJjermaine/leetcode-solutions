class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # min max algorithm
        # player 1 wants to minimize the amount of points player 2 gets
        # player 2 wants to maximize the number of points them themselves get

        min_num = float('inf')
        row1_sum = sum(grid[0])
        row2_sum = 0

        for col in range(len(grid[0])):
            row1_sum -= grid[0][col]
            min_num = min(min_num, max(row1_sum, row2_sum))
            row2_sum += grid[1][col]

        return min_num
