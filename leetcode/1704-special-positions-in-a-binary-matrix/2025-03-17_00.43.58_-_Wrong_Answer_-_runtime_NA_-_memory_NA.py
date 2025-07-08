class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        seenrow = [0] * rows
        seencol = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    seenrow[i] += 1
                    seencol[j] += 1
        res = 0
        for i in range(min(rows,cols)):
            if seencol[i] == 1 and seenrow[i] == 1:
                res += 1
        return res

