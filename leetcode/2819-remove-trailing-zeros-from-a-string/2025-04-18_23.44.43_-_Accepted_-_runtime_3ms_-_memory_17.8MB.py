class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != "0":
            return num
        
        r = len(num)-1
        while num[r] == "0":
            r -= 1
        return num[:r+1]
        