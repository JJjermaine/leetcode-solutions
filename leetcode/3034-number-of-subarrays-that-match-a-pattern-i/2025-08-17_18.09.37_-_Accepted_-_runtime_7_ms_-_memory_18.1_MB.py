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

        m = len(pattern)
        if m > len(res):
            return 0

        base, mod = 257, 10**9+7

        # Precompute powers
        power = [1] * (len(res)+1)
        for i in range(1, len(res)+1):
            power[i] = (power[i-1] * base) % mod

        # Prefix hashes of res
        prefix = [0] * (len(res)+1)
        for i in range(len(res)):
            prefix[i+1] = (prefix[i] * base + (res[i] + 2)) % mod
            # +2 shift to avoid negative values in hash

        # Hash of pattern
        pat_hash = 0
        for x in pattern:
            pat_hash = (pat_hash * base + (x + 2)) % mod

        def get_hash(l, r):
            """Hash of res[l:r] (r exclusive)."""
            return (prefix[r] - prefix[l] * power[r-l]) % mod

        # Count matches
        count = 0
        for i in range(len(res) - m + 1):
            if get_hash(i, i+m) == pat_hash:
                # Optional collision check
                if res[i:i+m] == pattern:
                    count += 1
        return count