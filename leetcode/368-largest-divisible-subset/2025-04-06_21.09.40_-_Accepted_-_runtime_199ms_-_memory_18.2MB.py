class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        res = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    if len(temp) > len(dp[i]):
                        dp[i] = temp
                    else:
                        dp[i]
            if len(dp[i]) > len(res):
                res = dp[i] 
            else:
                res
        return res
        