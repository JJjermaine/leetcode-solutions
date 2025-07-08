class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if max(nums)+1 >= len(nums):
            nums.sort()
            if nums[-1] == nums[-2]:
                return True
        return False
        