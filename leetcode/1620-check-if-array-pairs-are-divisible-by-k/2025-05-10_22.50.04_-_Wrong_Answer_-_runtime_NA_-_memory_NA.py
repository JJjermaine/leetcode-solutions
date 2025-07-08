class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # greedily match largest number with smallest number that will fulfill sum(largest, smallest) % k == 0
        arr.sort(reverse=True)
        d = Counter(arr)

        while d:
            largest = next(iter(d))
            smallest = (largest % k - k) * -1 # if k = 5, 124 % 5 = 4 --> 4 - k * -1 = 1 --> need for 1 to exist

            if d[-1 * largest]: # if [10, -10]
                d[-1 * largest] -= 1
                if d[-1 * largest] == 0:
                    del d[-1 * largest]

            elif d[smallest]:
                d[smallest] -= 1
                if d[smallest] == 0:
                    del d[smallest]

            else:
                return False

            d[largest] -= 1
            if d[largest] == 0:
                del d[largest]    

        return True

        