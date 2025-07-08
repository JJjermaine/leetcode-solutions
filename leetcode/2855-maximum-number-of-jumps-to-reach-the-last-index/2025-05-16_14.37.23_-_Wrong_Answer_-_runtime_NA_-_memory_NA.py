class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # dp
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if -1 * target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1] if dp[-1] > 0 else -1
            