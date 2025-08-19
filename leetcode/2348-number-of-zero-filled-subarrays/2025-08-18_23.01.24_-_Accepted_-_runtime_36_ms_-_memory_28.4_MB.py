class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # sliding window
        n = len(nums)
        curr = 0
        res = 0
        for r in range(n):
            if nums[r] == 0:
                curr += 1
            else:
                curr = 0
            res += curr
        return res