class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set((x, y) for x, y in points)
        res = float("inf")
        n = len(points)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    # Check if the other two corners exist
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        res = min(res, abs((x2 - x1) * (y2 - y1)))
        if res == float("inf"):
            return 0
        return res

                
                