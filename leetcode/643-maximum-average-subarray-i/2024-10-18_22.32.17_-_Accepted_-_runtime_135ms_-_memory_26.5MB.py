class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -10000000000
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while r - l >= k:
                curr -= nums[l]
                l += 1
            if r - l + 1 == k:
                res = max(res, curr / k)


        return res

            
        