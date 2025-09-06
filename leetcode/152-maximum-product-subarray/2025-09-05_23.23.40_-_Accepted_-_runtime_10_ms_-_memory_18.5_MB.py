class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # continous subarray so sliding window or dp
        # or greedily add number and if negative encountered, put it to the side until another negative comes
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
            
            res = max(res, curMax)
        return res
