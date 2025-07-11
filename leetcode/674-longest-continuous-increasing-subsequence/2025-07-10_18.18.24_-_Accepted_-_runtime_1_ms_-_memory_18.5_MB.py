class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        curr = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                curr = 1
            else:
                curr += 1
            res = max(res, curr)
        return res