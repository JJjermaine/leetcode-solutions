class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        res = [i for i in range(1, n+1)]
        curr = 0
        while len(res) > 1:
            curr += k - 1
            if curr > len(res)-1:
                curr %= len(res)
            res.pop(curr)

        return res[0]

        