class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # switch cases in terms of parsing from bottom left to top right or top right to bottom left
        # if cannot go bottom left to top right any further, switch to right else bottom
        # if cannot go top right to bottom left any further, switch to bottom else right
        topRight = True
        bottomLeft = False
        res = []
        rows = len(mat)
        cols = len(mat[0])
        row = 0
        col = 0

        def in_bounds(row, col):
            if row >= 0 and row < rows and col >= 0 and col < cols:
                return True
            else:
                return False

        while True:
            if topRight: # topRight parsing 
                res.append(mat[row][col])
                if in_bounds(row - 1, col + 1):
                    row -= 1
                    col += 1
                else:
                    if in_bounds(row, col + 1):
                        col += 1
                    else:
                        row += 1
                    topRight = False
            
            else: # bottom left parsing
                res.append(mat[row][col])
                if in_bounds(row + 1, col - 1):
                    row += 1
                    col -= 1
                else:
                    if in_bounds(row + 1, col):
                        row += 1
                    else:
                        col += 1

                    topRight = True
            if len(res) == rows * cols:
                break
        return res