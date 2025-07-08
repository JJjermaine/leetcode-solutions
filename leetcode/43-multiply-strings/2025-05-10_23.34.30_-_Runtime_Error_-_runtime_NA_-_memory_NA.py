class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        res = [0] * (len(num1) + len(num2))
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])

                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] %= 10
        while res[0] == 0:
            res.pop(0)
        return "".join(map(str, res))
                        
        