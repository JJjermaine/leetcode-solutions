class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # max possible XOR is 2^(maxBit) - 1
        xor = nums[0]
        max_xor = (1 << maximumBit) - 1

        for i in range(1, len(nums)):
            xor ^= nums[i]

        res = []
        for i in range(len(nums)-1, -1, -1):
            res.append(xor ^ max_xor)
            xor ^= nums[i]

        return res

        