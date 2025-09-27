class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Greedily remove the points that have the least amount of dependents
        # heap to keep track?

        # count dependents
        # dfs, if it can be reached, it can be removed
        # looked at sol
        n = len(stones)
        
        # build graph: stones connected if same row or column
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    visited.add(cur)
                    for nei in graph[cur]:
                        if nei not in visited:
                            stack.append(nei)
        
        # count connected components
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        # max stones removed = total stones - connected components
        return n - components

