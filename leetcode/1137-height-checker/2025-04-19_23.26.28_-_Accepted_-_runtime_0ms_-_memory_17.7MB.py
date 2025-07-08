class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != s[i]:
                res += 1
        return res

        