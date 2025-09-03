class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # needed help
        rows = len(matrix)
        cols = len(matrix[0])

        curr_row = rows-1
        curr_col = 0
        while 0 <= curr_col < cols and 0 <= curr_row < rows:
            if matrix[curr_row][curr_col] > target:
                curr_row -= 1
            elif matrix[curr_row][curr_col] < target:
                curr_col += 1
            else:
                return True
        return False