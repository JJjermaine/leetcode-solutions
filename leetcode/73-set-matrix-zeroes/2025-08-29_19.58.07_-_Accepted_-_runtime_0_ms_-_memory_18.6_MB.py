class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        setRows = [0] * rows
        setCols = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    setRows[i] = 1
                    setCols[j] = 1

        for i in range(rows):
            for j in range(cols):
                if setRows[i] == 1 or setCols[j] == 1:
                    matrix[i][j] = 0
