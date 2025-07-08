class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # get greatest difference of reward1[i] > reward2[i]
        # append whats left of reward2

        res = 0
        heap = []
        for i in range(len(reward1)):
            heap.append((reward2[i]-reward1[i], i))

        heapq.heapify(heap) # put largest difference first
        visited = set()
        while k: # make mouse1 eat value of largest difference index to maximize eating sum of mouse1 and mouse2
            k -= 1
            difference, index = heapq.heappop(heap)
            visited.add(index)
            res += reward1[index]

        for i in range(len(reward2)):
            if i not in visited:
                res += reward2[i]

        return res