class MedianFinder:

    def __init__(self):
        # 2 heaps, large (minheap) and small (maxheap) with equal size

        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num)

        if self.small and self.large and -1* self.small[0] > self.large[0]:
            val = -1 * heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) +1 :
            val = -1 * heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) +1 :
            val = heapq.pop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:
        # odd amount of elements
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        # even amount of elements
        return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()