class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        curr = 0
        for i in range(n-1,-1,-1):
            if curr == k:
                res += "-"
                curr = 0
            if s[i].isalpha():
                res += s[i].upper()
                curr += 1
            elif s[i].isnumeric():
                res += s[i]
                curr += 1
        res = res[::-1]
        if res[0] == "-":
            return res[1:]
        return res


