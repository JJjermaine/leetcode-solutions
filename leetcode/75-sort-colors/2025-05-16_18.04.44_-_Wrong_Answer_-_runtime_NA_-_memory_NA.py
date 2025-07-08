class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        twos = 0
        i = 0
        while i < len(nums):
            if nums[i] == 2:
                twos += 1
                nums.pop(i)
            i += 1
        while twos != 0:
            nums.append(2)
            twos -= 1

        i = len(nums)-1
        zeros = 0
        while i > 0:
            if nums[i] == 0:
                zeros =+ 1
                nums.pop(i)
            i -= 1
        while zeros != 0:
            nums.insert(0, 0)
            zeros -= 1