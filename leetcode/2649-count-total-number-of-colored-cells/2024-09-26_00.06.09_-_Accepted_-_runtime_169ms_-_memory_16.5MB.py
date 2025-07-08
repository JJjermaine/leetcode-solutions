class Solution:
    def coloredCells(self, n: int) -> int:
        pattern = 0
        res = 1
        for i in range(n):
            res += pattern
            pattern += 4

        return res
        