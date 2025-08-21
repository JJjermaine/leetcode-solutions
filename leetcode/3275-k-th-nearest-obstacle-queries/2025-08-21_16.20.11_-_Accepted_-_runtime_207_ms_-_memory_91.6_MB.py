class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        # get kth smallest obstacle
        # min heap
        # needed help from gpt
        res = []
        heap = []  # max-heap (store negatives)

        for x, y in queries:
            dist = abs(x) + abs(y)

            if len(heap) < k:
                heapq.heappush(heap, -dist)
            else:
                if dist < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -dist)

            if len(heap) < k:
                res.append(-1)
            else:
                res.append(-heap[0])

        return res

