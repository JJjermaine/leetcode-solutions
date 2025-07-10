class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # min of the surrounding + 1

        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):

                
        res = [[0] * rows for _ in range(cols)]
                if mat[i][j] == 1:
                smallest = float("inf")
                        smallest = min(smallest, mat[i][j+1])
                        smallest = min(smallest, mat[i+1][j])
                        smallest = min(smallest, mat[i][j-1])
                        smallest = min(smallest, mat[i-1][j])
                    if i > 0:
                    if j > 0:
                    if i < rows-1:
                    if j < cols-1:
                    res[i][j] = smallest + 1
        return res
