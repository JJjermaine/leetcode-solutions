class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force
        dp_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_arr[i] = max(dp_arr[i], 1+dp_arr[j])

        return max(dp_arr)

        