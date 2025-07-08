class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # Double the original string to form a new string (s + s)
        # If s is a repeated substring, it will exist in (s + s) except the first and last character
        new_string = s + s
        return s in new_string[1:-1]