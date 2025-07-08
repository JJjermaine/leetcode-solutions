class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        l, r = 0, len(mat)-1
        for i in range(len(mat)):
            if l == r:
                res += mat[i][l]
            else:
                res += mat[i][l] + mat[i][r]
            l += 1
            r -= 1
        return res
            