class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        heap = [1]
        visited = set()
        visited.add(1)
        for i in range(n):
            curr = heapq.heappop(heap)
            for num in primes:
                new = curr * num
                if new not in visited:
                    heapq.heappush(heap, new)
                    visited.add(new)
        return curr