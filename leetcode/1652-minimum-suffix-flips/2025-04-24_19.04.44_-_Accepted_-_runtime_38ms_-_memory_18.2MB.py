class Solution:
    def minFlips(self, target: str) -> int:
        # count each block of ones and zeros
        # if just ones, res is 1
        # if just zeros, res is 0


        if all(target[i] == "0" for i in range(len(target))):
            return 0

        res = 1
        r = len(target)-1
        prev = target[-1]

        while r >= 0:
            if target[r] == "1":
                if prev == 0:
                    res += 1
                prev = 1
            if target[r] == "0":
                if prev == 1:
                    res += 1
                prev = 0
            r -= 1
        
        # if starting is 0, res -= 1
        if target[0] == "0":
            res -= 1
        return res


        