class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # greedily take the largest number and perform floor(piles[i]/2)
        pq = []
        for num in piles:
            heapq.heappush(pq, -1 * num) # make it negative so you can access largest number

        for i in range(k):
            val = heapq.heappop(pq) # largest element
            val = math.floor(val/2)
            heapq.heappush(pq, val)

        return sum(-1 * num for num in pq)
        