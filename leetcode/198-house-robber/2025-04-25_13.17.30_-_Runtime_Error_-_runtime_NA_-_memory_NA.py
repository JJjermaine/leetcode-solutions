class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp, option where you do rob vs skip
        n = len(nums)
        # edge case, n == 1
        if n == 1:
            return nums[0]

        # edge case, n == 3
        if n == 3:
            return max(nums[0] + nums[2], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        for i in range(3, n):
            dp[i] = max(nums[i] + max(dp[i-2], dp[i-3]),  dp[i-1])
        return dp[-1]