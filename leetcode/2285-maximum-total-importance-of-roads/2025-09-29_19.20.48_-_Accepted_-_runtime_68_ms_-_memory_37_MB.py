class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # greedily assign the least connections with the least value
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        # sort nodes by degree
        nodes = sorted(range(n), key=lambda x: degree[x])
        
        # assign importance values
        values = [0] * n
        importance = 1
        for node in nodes:
            values[node] = importance
            importance += 1
        
        # calculate result
        res = 0
        for u, v in roads:
            res += values[u] + values[v]
        
        return res

        
        
