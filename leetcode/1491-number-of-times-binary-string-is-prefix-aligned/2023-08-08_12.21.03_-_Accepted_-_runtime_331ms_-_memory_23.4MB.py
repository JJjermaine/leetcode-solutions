class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
            rightmax = -1
            count = 0
            for i in range(len(flips)):
                if flips[i] > rightmax:
                    rightmax = flips[i]
                if rightmax == i + 1:
                    count += 1
            return count