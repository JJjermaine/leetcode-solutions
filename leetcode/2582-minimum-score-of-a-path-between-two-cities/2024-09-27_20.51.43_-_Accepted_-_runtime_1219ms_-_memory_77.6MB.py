class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # not my work
        # problem: get smallest edge score
        # bfs to get min score

        graph = defaultdict(dict)
        for start, end, score in roads:
            graph[start][end] = score
            graph[end][start] = score

        res = float('inf')
        visited = set()
        dq = deque([1]) # start at city 1

        while dq:
            node = dq.popleft()
            for adj, scr in graph[node].items():
                if adj not in visited: # while each node from hasnt been visited
                    dq.append(adj)
                    visited.add(adj) 
                res = min(res, scr) # check if current edge or our edge is smaller

        return res
        