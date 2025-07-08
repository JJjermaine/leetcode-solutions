class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            # window length = (r - l + 1)
            while (r - l + 1) - max(count.values()) > k: # window length minus max count in dictionary
            # ^ This represents max replacements
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
                
        return res




        