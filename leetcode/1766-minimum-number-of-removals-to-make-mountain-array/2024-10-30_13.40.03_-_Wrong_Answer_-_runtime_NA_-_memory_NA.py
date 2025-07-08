class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # have longest increasing and decreasing subsequence

        LIS = [1] * len(nums)
        LDS = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        
        res = len(nums)
        for i in range(1, len(nums)-1):
            if LIS[i] > 1 or LDS[i] > 1:
                res = min(res, len(nums) - LIS[i] - LDS[i] + 1)

        return res