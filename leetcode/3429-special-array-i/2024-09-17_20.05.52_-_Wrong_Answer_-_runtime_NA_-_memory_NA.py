class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)-1):

            if nums[i] % 2 == 0: # even
                return nums[i-1] % 2 != 0 and nums[i+1] % 2 != 0

            else: #odd
                return nums[i-1] % 2 == 0 and nums[i+1] % 2 == 0
