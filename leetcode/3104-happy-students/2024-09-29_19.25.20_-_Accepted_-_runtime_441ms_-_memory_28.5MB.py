class Solution:
    def countWays(self, nums: List[int]) -> int:
        # ans not my own
        # nums[i] must be less than i + 1 and i + 1 must be less than nums[i+1]
        nums.sort()
        nums.append(float('inf'))
        
        if nums[0] != 0:
            res = 1
        else: res = 0

        for i in range(len(nums)):
            if nums[i] < (i + 1) < nums[i+1]:
                res += 1

        return res
        