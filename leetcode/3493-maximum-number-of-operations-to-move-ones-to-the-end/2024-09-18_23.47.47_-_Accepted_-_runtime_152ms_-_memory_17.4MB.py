class Solution:
    def maxOperations(self, s: str) -> int:
        onesCount = 0
        ans = 0
        prevBit = -1

        for i in range(len(s)):
            bit = int(s[i])
            onesCount += bit
            if bit == 0 and prevBit==1:
                ans += onesCount
            prevBit = bit

        return ans