class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n  == 0 or m == 0:
            return 0
        if n == 1:
            return 1
        if m == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)