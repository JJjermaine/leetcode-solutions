class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        count = {}

        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        min_len = len(s)

        for key, value in count.items():
            while value >= 3:
                value -= 2
                min_len -= 2

        return min_len




        
        