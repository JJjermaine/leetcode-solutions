class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window + dp?
        n = len(nums)
        largest = 0 
        curr = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                curr += 1    
            while curr > k:
                if nums[l] == 0:
                    curr -= 1
                l += 1

            largest = max(largest, r - l + 1)
        return largest
        