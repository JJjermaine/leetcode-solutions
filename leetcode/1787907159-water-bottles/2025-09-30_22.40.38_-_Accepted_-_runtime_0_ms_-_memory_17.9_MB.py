class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        remainder = 0
        while numBottles > 0:
            res += numBottles
            print(numBottles)
            numBottles += remainder
            remainder = numBottles % numExchange
            numBottles //= numExchange

            
        return res