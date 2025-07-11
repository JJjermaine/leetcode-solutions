class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # get min of ops because its always increased at that point
        if not ops:
            return n * m

        min_a = m
        min_b = n

        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b
        