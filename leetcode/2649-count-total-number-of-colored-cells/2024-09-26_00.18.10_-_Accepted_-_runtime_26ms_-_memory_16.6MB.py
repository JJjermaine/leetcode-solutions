class Solution:
    def coloredCells(self, n: int) -> int:
        # cut and combine 2 parts
        # cut top half to get n * n square, cut bottom half to get n-1 *n-1 square
        top = n * n 
        bottom = (n - 1) * (n - 1)

        return top + bottom
        