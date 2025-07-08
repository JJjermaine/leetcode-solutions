class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = nums[i] * nums[j]
                res += count.get(key, 0)
                count[key] = 1 + count.get(key, 0)

        return res * 8

        