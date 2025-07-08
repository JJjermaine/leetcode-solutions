class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        # traverse from lext to right
        for j in range(1, cols):
            for i in range(rows):
                max_moves = 0
                
                # Move from (i, j-1) if value is greater
                if grid[i][j] > grid[i][j - 1] and dp_matrix[i][j] != -1:
                    max_moves = max(max_moves, dp_matrix[i][j - 1] + 1)
                
                # Move from (i - 1, j-1) if within bounds and value is greater
                if i > 0 and grid[i][j] > grid[i - 1][j - 1] and dp_matrix[i][j] != -1:
                    max_moves = max(max_moves, dp_matrix[i - 1][j - 1] + 1)
                
                # Move from (i + 1, j-1) if within bounds and value is greater
                if i < rows - 1 and grid[i][j] > grid[i + 1][j - 1] and dp_matrix[i][j] != -1:
                    max_moves = max(max_moves, dp_matrix[i + 1][j - 1] + 1)
                
                # Update the dp_matrix with maximum moves from this cell
                if max_moves == 0:
                    dp_matrix[i][j] = -1
                else:
                    dp_matrix[i][j] = max_moves

        return max(max(x) for x in dp_matrix)
