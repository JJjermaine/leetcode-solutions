class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs on each one and if not visited, +1 to result
        n = len(isConnected)
        visited = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
                visited.add(i)
        return res
        