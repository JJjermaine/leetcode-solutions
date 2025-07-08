class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(s, 0) + 1

        for key, value in count.items():
            if value >= 2:
                value -= 2
        
        return sum(count.values())
        