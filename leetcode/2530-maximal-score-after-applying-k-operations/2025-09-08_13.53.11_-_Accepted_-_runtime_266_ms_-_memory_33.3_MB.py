class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # greedily take the highest scores via heap?

        max_heap = [-n for n in nums] 
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            val = -heapq.heappop(max_heap)
            res += val
            val = math.ceil(val / 3)
            heapq.heappush(max_heap, -val)
        return res
