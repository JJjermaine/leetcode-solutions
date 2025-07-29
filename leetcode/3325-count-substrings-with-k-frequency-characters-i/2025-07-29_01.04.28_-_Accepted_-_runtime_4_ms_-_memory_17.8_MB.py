class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        # example 1: once 2 chars appears, count n - r
        # example 2: 5 + 4 + 3 + 2 + 1

        # strat: once k chars appear, count n - r
        # and slide r pointer to end first, then l pointer to end

        # needed help to finish
        n = len(s)
        l = 0
        d = defaultdict(int)
        res = 0
        has_k_freq = False

        for r in range(n):
            d[s[r]] += 1

            # Check if any char hits k frequency
            if d[s[r]] == k:
                has_k_freq = True

            # Slide l to maintain minimal valid window
            while has_k_freq:
                res += n - r  # all substrings [l..r], [l+1..r], ... [r..r] are valid
                d[s[l]] -= 1

                # If we lose the k-frequency char, mark it invalid
                if d[s[l]] == k - 1:
                    has_k_freq = False
                l += 1
        return res
