class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], nums[i])

        # maximize i - j and maximize k where i < j < k
        res = 0
        for i in range(1, len(nums)-1):
            curr = (prefix[i-1] - nums[i]) * suffix[i+1]
            res = max(res, curr)
        return res


        