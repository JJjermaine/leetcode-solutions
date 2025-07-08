class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window + dp?
        n = len(nums)
        dp = [0] * n 
        curr = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                curr += 1    
            while curr > k:
                if nums[l] == 0:
                    curr -= 1
                l += 1

            dp[r] = max(dp[r-1], r - l + 1)
        return dp[-1]
        