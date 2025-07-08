class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            sumSides = nums[i] +nums[i+1]
            if sumSides > nums[i+2]:
                perm = nums[i]+nums[i+1]+nums[i+2]
                ans = max(perm,ans)
        return ans
        