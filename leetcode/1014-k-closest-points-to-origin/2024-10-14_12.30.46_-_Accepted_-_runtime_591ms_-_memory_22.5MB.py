class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = math.sqrt((x * x) + (y * y))
            distances.append((dist, i))

        distances.sort()
        res = []
        for i in range(k):
            res.append(points[distances[i][1]])

        return res

