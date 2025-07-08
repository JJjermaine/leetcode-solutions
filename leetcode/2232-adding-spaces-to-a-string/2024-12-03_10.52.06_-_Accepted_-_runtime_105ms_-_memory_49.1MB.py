class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        spaces.append(0)
        p = 0
        for i in range(len(s)):
            if i == spaces[p]:
                res += " "
                p += 1
            res += s[i]
        return res
        