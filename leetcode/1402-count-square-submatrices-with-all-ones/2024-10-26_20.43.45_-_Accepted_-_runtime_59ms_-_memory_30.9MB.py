import numpy as np
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
            n = len(matrix)    
            m = len(matrix[0]) 
            
            # Create a DP table with same dimensions as matrix
            dp_matrix = [[0] * m for _ in range(n)]
            
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == 1:
                        if i > 0 and j > 0:
                            dp_matrix[i][j] = min(dp_matrix[i-1][ j], dp_matrix[i][j-1], dp_matrix[i-1][j-1]) + 1
                        else:
                            dp_matrix[i][j] = 1
            
            return sum(sum(arr) for arr in dp_matrix)