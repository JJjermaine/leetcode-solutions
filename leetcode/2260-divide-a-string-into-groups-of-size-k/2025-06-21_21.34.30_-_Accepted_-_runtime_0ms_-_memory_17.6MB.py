class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        curr = ""
        for i in range(len(s)):
            if len(curr) == k:
                res.append(curr)
                curr = ""
            curr += s[i]

        if len(curr) > 0:
            while len(curr) < k:
                curr += fill
            res.append(curr)
        return res
        