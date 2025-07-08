class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

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
            
            if largest < smallest * 2 and sc == 2 or largest * 2 > smallest and lc == 2:
                return "isosceles"

        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a + b > c and a + c > b and b + c > a:
            return "scalene"



        return "none"

        