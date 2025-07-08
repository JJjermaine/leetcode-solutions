class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"


        largest = max(nums)
        squared = 0
        for i in range(len(nums)):
            if nums[i] != largest:
                squared += nums[i] * nums[i]
        if squared == largest * largest:
            return "scalene"

        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            smallest = min(nums)
            largest = max(nums)
            sc = 0
            lc = 0
            for num in nums:
                if num == smallest:
                    sc += 1
                else:
                    lc += 1
            
            if largest < smallest * 2 and sc == 2 or largest > smallest * 2 and lc == 2:
                return "isosceles"

        return "none"

        