class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            onesRow = sum(grid[i])
            zerosRow = cols - onesRow
            for j in range(cols):
                new_matrix[i][j] = (onesRow - zerosRow) 

        for j in range(cols):
            onesCol = 0
            for i in range(rows):
                onesCol += grid[i][j]
            zerosCol = rows - onesCol
            for i in range(rows):
                new_matrix[i][j] += (onesCol - zerosCol)
        return new_matrix