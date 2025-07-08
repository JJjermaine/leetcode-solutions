class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                idx = i
            

        for i in range(len(nums)):
            if i == idx:
                continue
            if max_val < nums[i] * 2:
                return -1

        return idx
        