class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        stones = stones[::-1]

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            stones.append(abs(first - second))

        return stones[0]

        
        