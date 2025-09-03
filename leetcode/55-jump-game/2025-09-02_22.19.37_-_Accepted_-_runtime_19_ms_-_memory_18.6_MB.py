class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedily take the one that can take you the furthest
        n = len(nums)
        left = nums[0]
        for i in range(1, n):
            left -= 1
            if nums[i] > left and left >= 0:
                left = nums[i]
        
        return True if left >= 0 else False


