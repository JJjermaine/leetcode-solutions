class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_distinct = len(set(nums))
        d = defaultdict(int)
        res = 0
        l = 0

        for r in range(n):
            d[nums[r]] += 1

            while len(d) == total_distinct:
                # All subarrays [l, r], [l+1, r], ..., [r, r] are valid
                res += (n - r)
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
        return res


        