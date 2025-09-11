class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # bfs on each path? would that result in TLE?
        # gpt said yes, and said dfs with dp is the solution
        # from example 1:
        # the dp array should look like
        # [1, 1, 2]
        # [2, 2, 1]
        # [3, 4, 2]

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for i in range(rows)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
        
            val = matrix[i][j]
            best = 1
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for x, y in directions:
                new_x = i + x
                new_y = j + y
                if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] > val:
                    best = max(best, 1 + dfs(new_x, new_y))

            dp[i][j] = best
            return best

        best = 1
        for i in range(rows):
            for j in range(cols):
                best = max(dfs(i, j), best)
        return best