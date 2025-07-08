class Solution:
    def generateTheString(self, n: int) -> str:
        
        res = ""
        if n % 2 != 0:
            for i in range(n):
                res += "a"

        else:
            for i in range(n-1):
                res += "a"
            res += "b"

        return res