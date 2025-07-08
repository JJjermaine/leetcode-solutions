class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        s = set()
        n = len(matrix)
        d = set()
        for i in range(n):
            for j in range(n):
                s.add(matrix[i][j])
                d.add(matrix[j][i])
            if len(s) != n or len(d) != n:
                return False
            s = set()
            d = set()
        return True

