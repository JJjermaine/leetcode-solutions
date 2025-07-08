class Solution:
    def isGood(self, nums: List[int]) -> bool:
        s = sorted(nums)
        new = list(range(1, len(nums))) + [len(nums)-1] # ex: len(nums) = 6 will make new = [1, 2, 3, 4, 5, 5]

        if s == new:
            return True
        return False
        