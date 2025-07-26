class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # just add the sum of set
        unique_nums = set()
        minimum_neg = float("-inf")
        for i in range(len(nums)):
            if nums[i] >= 0:
                unique_nums.add(nums[i])
            else:
                minimum_neg = max(minimum_neg, nums[i])

        if len(unique_nums) > 0:
            return sum(unique_nums)
        return minimum_neg