class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s = s + " "
        if len(s) == 2:
            return []
        l, r = 0, 1
        res = []
        # 2 pointer
        while r < len(s)-1:
            while s[l] != s[r] and r < len(s)-1:
                l += 1
                r += 1
            while s[l] == s[r] and r < len(s)-1:
                r += 1
            curr = r - l - 1
            if curr >= 2:
                res.append([l, r-1])
            l = r - 1
        return res

            
            
            
        