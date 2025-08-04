class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        n = len(fruits)
        l = 0
        largest = 0
        for r in range(n):
            d[fruits[r]] += 1

            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            
            largest = max(largest, r - l + 1)

        return largest
            
            

