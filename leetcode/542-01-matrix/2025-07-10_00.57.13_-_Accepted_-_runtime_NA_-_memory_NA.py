class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # min of the surrounding + 1

        rows = len(mat)
        cols = len(mat[0])
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                smallest = float("inf")
                if mat[i][j] == 1:
                    if j < cols-1:
                        smallest = min(smallest, mat[i][j+1])
                    if i < rows-1:
                        smallest = min(smallest, mat[i+1][j])
                    if j > 0:
                        smallest = min(smallest, mat[i][j-1])
                    if i > 0:
                        smallest = min(smallest, mat[i-1][j])
                    res[i][j] = smallest + 1
        return res
                
