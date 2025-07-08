class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_string = s+s
        return s in new_string[1:-1]
