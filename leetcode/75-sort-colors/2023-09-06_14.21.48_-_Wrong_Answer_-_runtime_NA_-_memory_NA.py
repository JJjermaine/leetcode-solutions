class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerocount = 0
        onecount = 0
        twocount = 0

        for num in nums:
            if num == 0:
                zerocount += 1
            elif num == 1:
                onecount += 1
            else:
                twocount += 1

        for i in range(zerocount):
            nums[i] = 0
        for i in range(zerocount, len(nums) - onecount):
            nums[i] = 1
        for i in range(zerocount + onecount, len(nums)):
            nums[i] = 2
        

        