class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        largest = max(nums)
        count = 0  # counts how many times we've seen 'largest' in the current window
        left = 0
        res = 0
        
        for right, val in enumerate(nums):
            if val == largest:
                count += 1
            
            # If there are at least k 'largest' in the window [left..right], count subarrays
            while count >= k:
                if nums[left] == largest:
                    count -= 1
                left += 1
            
            # Add the number of valid subarrays ending at 'right'
            res += left
        
        return res
            

            
