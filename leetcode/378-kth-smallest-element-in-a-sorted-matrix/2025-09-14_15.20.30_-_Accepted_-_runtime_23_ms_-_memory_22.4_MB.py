class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                heapq.heappush(heap, -matrix[i][j])

        for i in range(rows * cols - k):
            heapq.heappop(heap)
                
        return -heap[0]