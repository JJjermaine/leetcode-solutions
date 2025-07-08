class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and nums[j] + nums[k] > nums[i] and nums[i] + nums[k] > nums[j]:
                        largest = max(largest, nums[i] + nums[j] + nums[k])
        return largest
        