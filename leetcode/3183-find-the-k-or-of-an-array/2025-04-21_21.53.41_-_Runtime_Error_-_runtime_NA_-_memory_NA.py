class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        total = [0] * 6
        res = ""
        for num in nums:
            curr = bin(num)[2:]
            add = 5
            for i in range(len(curr)-1,-1,-1):
                if curr[i] == "1":
                    total[add] += 1
                add -= 1
        for i in range(len(total)-1,-1,-1):
            if total[i] >= k:
                res += "1"
            else:
                res += "0"
        return int(res[::-1], 2)



        