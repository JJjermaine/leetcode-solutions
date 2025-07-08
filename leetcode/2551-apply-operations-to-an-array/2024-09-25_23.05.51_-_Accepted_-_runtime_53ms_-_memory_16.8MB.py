class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # after all operations applied, simply put the non zero integers to the left
        count = 0
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                count += 1

        for i in range(count):
            res.append(0)

        return res

        
        