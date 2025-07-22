class Solution:
    def makeFancyString(self, s: str) -> str:

        res = ""
        prev = [[s[0], 0]]
        for i in range(len(s)):
            if prev[0][0] == s[i]:
                prev[0][1] += 1
            else:
                prev = [[s[i], 1]]
            
            if prev[0][1] < 3:
                res += s[i]
            
        return res