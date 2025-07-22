class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # sliding window
        l = 0
        n = len(nums)
        curr = 0
        largest = 0
        d = defaultdict(int)
        for r in range(n):
            while d[nums[r]]:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                curr -= nums[l]    
                l += 1
                
            else:
                d[nums[r]] += 1
                curr += nums[r]
            largest = max(largest, curr)
        return largest



