class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            m = (l + r) // 2
            totalTime = 0

            for bananas in piles:
                totalTime += math.ceil(float(bananas) / m)

            if totalTime <= h:
                res = m
                r = m - 1
            elif totalTime > h:
                l = m + 1
        return res
        