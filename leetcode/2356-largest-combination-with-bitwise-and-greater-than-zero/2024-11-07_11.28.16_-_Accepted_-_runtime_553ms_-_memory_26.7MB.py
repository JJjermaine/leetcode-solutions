class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for candidate in candidates:
                if candidate & (1 << i):
                    count += 1
            res = max(count, res)

        return res