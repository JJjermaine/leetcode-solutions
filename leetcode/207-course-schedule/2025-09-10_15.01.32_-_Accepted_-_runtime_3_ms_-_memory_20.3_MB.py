class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs to make sure num courses match the number of dfs traversals
        # Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()     # nodes fully processed (safe)
        visiting = set()    # nodes in current DFS path (to detect cycle)

        def dfs(node):
            if node in visiting:   # cycle found
                return False
            if node in visited:    # already processed
                return True

            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        # Check all courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True