class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # have a heap to only add to highest ratio
        res = 0
        n = len(classes)
        track = [0] * n

        for i in range(n):
            p = classes[i][0]
            t = classes[i][1]
            track[i] = [-(((p+1) / (t+1)) - (p / t)), p, t]
            res += p / t

        heapq.heapify(track)

        for i in range(extraStudents):
            res += -track[0][0]
            p = track[0][1]
            t = track[0][2]
            new = [-(((p+2) / (t+2)) - ((p+1) / (t+1))), p+1, t+1]
            heapq.heappop(track)
            heapq.heappush(track, new)
        
        return res / len(classes)
