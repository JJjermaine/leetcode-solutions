class Solution:
    def minimumChairs(self, s: str) -> int:
        curr = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "E":
                curr += 1
            else:
                curr -= 1
            res = max(res, curr)
        return res