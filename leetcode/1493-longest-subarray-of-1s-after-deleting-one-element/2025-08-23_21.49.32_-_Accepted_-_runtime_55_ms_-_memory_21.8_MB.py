class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window
        n = len(nums)
        largest = 0
        l = 0
        zeroes = 0
        for r in range(n):
            if nums[r] == 0:
                zeroes += 1

                if zeroes > 1:
                    l = most_recent_one
                    zeroes -= 1
            
                most_recent_one = r + 1

                
            largest = max(largest, r - l)
        return largest
