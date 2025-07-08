class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        count = 0
        while count < len(nums)-1:
            if nums[index] == 0:
                nums.append(nums.pop(index))
                index -= 1
            index += 1
            count += 1

        """
        Do not return anything, modify nums in-place instead.

        [0,1,0,3,12]

        [1,0,3,12,0]

        [1,3,12,0,0]
        """