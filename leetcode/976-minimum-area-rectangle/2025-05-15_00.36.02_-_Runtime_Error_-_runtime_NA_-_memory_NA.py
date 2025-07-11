class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float("inf")
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y2) in seen and (x2, y1) in seen:
                res = min(res, abs((x2-x1) * (y2-y1)))
            seen.add((x1, y1))
        if res == float("inf"):
            return 0
        return res

                
                