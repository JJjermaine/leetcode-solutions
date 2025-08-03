class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        if len(s) < 2:
            return False

        revStr = s[::-1]
        d = defaultdict(int)
        for i in range(1, len(s)):
            substr = revStr[i-1] + revStr[i]
            d[substr] += 1
        
        for i in range(1, len(s)):
            substr = s[i-1] + s[i]
            if d[substr]:
                return True

        return False
