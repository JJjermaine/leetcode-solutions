class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(len(s)-1):
            value = ord(s[i])
            adj_value = ord(s[i+1])

            res += abs(value - adj_value)

        return res

        