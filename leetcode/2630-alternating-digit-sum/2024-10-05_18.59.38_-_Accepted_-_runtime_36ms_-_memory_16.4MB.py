class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        string = str(n)
        for i in range(len(string)):
            if i % 2 == 0:
                res += int(string[i])
            else:
                res -= int(string[i])

        return res
        