class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            if nums[i] == 0: 
                    nums.append(nums.pop(i))
        """
        Do not return anything, modify nums in-place instead.
        """