class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        count=0
        while count < len(nums)-1:
            if nums[i] == 0: 
                    nums.append(nums.pop(i))
                    i-=1
            i+=1
            count+=1
        """
        Do not return anything, modify nums in-place instead.
        """