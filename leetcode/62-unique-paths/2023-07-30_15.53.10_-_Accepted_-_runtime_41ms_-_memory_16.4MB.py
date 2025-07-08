class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = m - 1
        y = n - 1
        res = 1
        for i in range (1, x+1):
            res = res * (y + i) / i
        return int(res)