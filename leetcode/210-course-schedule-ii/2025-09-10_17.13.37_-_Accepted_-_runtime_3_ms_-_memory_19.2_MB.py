class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs, sort by levels and add them by levels, make sure no cycles aswell
        adjacency_list = [0] * numCourses
        graph = defaultdict(list)
        for u, v in prerequisites: # [[1,0],[2,0],[3,1],[3,2],[2,4]] turns into 
            graph[v].append(u) # 0: [1, 2]  1: [3]  2: [3]  3: []  4: [2]
            adjacency_list[u] += 1 # [0,1,2,2,0]

        #for u, v in prerequisites: 
        #    adjacency_list[u] += 1 

        queue = deque()
        for i in range(numCourses): # all with 0
            if adjacency_list[i] == 0:
                queue.append(i) # queue = [0, 4]

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                adjacency_list[nei] -= 1
                if adjacency_list[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []

