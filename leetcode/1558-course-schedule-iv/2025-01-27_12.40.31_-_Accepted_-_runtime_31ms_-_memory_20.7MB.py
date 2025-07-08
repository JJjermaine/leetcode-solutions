class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                for prereq in adj[course]:
                    prereqMap[course] |= dfs(prereq)
                prereqMap[course].add(course)
            return prereqMap[course]

        prereqMap = {} 
        for course in range(numCourses):
            dfs(course)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res