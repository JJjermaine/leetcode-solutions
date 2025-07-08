class Solution:
    def sortSentence(self, s: str) -> str:
        res = []
        s = s.split()
        for i in range(len(s)):
            for j in range(len(s)):
                x = int(s[j][-1])
                if x == i+1:
                    res.append(s[j][0:-1])
        return " ".join(res)

        