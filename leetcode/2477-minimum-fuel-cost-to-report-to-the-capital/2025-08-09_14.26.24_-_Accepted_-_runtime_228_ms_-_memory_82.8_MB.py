class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        # dfs to the last nodes and start counting from there
        # needed help from gpt

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        track = set()
        self.fuel = 0

        def dfs(node, parent):
            people = 1
            for nei in graph[node]:
                if nei != parent:
                    sub_people = dfs(nei, node)
                    # Cars needed from subtree to parent
                    self.fuel += math.ceil(sub_people / seats)
                    people += sub_people
            return people



        dfs(0, -1)
        return self.fuel