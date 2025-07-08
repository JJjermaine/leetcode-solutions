class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedily take 1's from the right, greedily take all 0's
        n = len(s)
        res = 0
        curr = 0
        ptr = 1
        stop_counting_ones = False
        for i in range(n-1,-1,-1):
            if not stop_counting_ones:
                if s[i] == "1":
                    curr += ptr
                    if curr > k:
                        stop_counting_ones = True
                        continue
                    res += 1

            if s[i] == "0":
                res += 1
            
            ptr *= 2

        return res