class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        n = len(graph)

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            safe[i] = True
            return True

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res