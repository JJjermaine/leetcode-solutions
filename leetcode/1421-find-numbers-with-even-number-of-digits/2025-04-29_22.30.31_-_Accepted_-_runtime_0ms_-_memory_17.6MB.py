class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                res += 1
        return res
        