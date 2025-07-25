class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p[0] == "*":
            if p[1:len(p)] in s:
                return True
            else:
                return False
        if p[-1] == "*":
            if p[:len(p)-1] in s:
                return True
            else:
                return False
        index = 0
        first = ""
        second = ""
        switch = True
        for i in range(len(p)):
            if p[i] == "*":
                switch = False
                continue
            if switch:
                first += p[i]
            else:
                second += p[i]

        for i in range(len(s)):
            if first in s[:i] and second in s[i:]:
                return True
        return False
