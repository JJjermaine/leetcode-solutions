class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            averages.append((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1

        return min(averages)
        