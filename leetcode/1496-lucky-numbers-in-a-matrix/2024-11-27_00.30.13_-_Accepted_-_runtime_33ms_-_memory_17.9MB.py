class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        min_row = []
        max_col = []
        for row in range(rows):
            curr_min = float('inf')
            for col in range(cols):
                curr_min = min(curr_min, matrix[row][col])
            min_row.append(curr_min)

        for col in range(cols):
            curr_max = float('-inf')
            for row in range(rows):
                curr_max = max(curr_max, matrix[row][col])
            max_col.append(curr_max)

        res = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] in min_row and matrix[row][col] in max_col:
                    res.append(matrix[row][col])

        return res

        