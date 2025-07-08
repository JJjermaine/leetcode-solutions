class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0
        for c in s:
            if c == "0":
                zeros += 1
            else:
                ones += 1

        res = ""
        while ones > 1 or zeros:
            if ones > 1:
                res += "1"
                ones -= 1
            else:
                res += "0"
                zeros -= 1
        if ones == 1:
            res += "1"


        return res

        


        