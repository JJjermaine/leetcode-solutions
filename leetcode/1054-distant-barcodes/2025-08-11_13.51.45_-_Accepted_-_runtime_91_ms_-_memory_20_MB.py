class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # greedily add res[i] as the highest amount that isnt the same as res[i-1]
        # needed to look at sols
        result = []
        counts = Counter(barcodes)
        
        # Create a max-heap based on count
        heap = [[-v, k] for k, v in counts.items()]
        
        heapq.heapify(heap)
        
        # Get the first item
        item = heapq.heappop(heap)

        while heap:
            result.append(item[1])
            item[0] += 1 # "Decrease" the count
            if item[0] < 0:
                item = heapq.heapreplace(heap, [item[0], item[-1]])
            else:
                item = heapq.heappop(heap)

        # Because I do a `heappop` outside of the while loop, we should append the last element!
        result.append(item[1])
        return result