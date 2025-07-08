class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        consec = 1
        res = 0
        for i in range(n):
            if s[i] == "0":
                consec = 1
            else:
                res += consec
                consec += 1
        return res % 1000000007

        