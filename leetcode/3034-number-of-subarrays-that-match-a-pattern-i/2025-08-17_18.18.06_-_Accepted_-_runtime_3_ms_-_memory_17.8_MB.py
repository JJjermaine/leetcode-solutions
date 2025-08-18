class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # needed to look at gpt solution
        n = len(nums)
        res = [0] * (n-1)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                res[i] = -1
            elif nums[i] < nums[i+1]:
                res[i] = 1
            else:
                res[i] = 0

        count = 0
        for i in range(n - len(pattern) + 1):
            count += res[i:i+len(pattern)] == pattern

        return count