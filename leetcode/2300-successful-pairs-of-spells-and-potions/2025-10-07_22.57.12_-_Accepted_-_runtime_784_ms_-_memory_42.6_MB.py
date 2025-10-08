class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # brute force is going through each spell and potion and seeing if > than success
        potions.sort()
        res = []
        for i in range(len(spells)):
            lo = 0
            hi = len(potions)-1
            while lo <= hi:
                mid = (lo + hi) // 2
                if potions[mid] * spells[i] >= success:
                    hi = mid - 1
                else:
                    lo = mid + 1

            res.append(len(potions) - lo)
        return res