class Solution:
    def findLatestTime(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # ten hour
            if i == 0:
                if s[i] == "?":
                    res += "1"
                else:
                    res += s[i]

            # one hour
            if i == 1:
                if s[i] == "?" and res[i-1] == "1":
                    res += "1"
                elif s[i] == "?":
                    res += "9"
                else:
                    res += s[i]
            
            # semi colon
            if i == 2:
                res += ":"

            # ten minute
            if i == 3:
                if s[i] == "?": 
                    res += "5"
                else: 
                    res += s[i]

            # one minute
            if i == 4:
                if s[i] == "?":
                    res += "9"
                else:
                    res += s[i]
        return res

        