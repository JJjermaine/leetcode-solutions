class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window?
        # [2, 3, 1, 2, 4, 3]
        n = len(nums)
        curr = 0
        res = float('inf')
        l = 0
        for r in range(n):
            while curr > target:
                res = min(res, r - l)
                curr -= nums[l]
                l += 1

            curr += nums[r]
        while curr > target or l >= n:
            res = min(res, r - l)
            curr -= nums[l]
            l += 1

        return 0 if res == float('inf') else res

