class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0

        l = 0
        r = len(nums)-1

        while l < r:
            res += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1

        # handle middle indices
        if len(nums) % 2 != 0: # odd length 
            res += nums[(len(nums) // 2)]

        return res
        