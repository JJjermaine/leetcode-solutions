class Solution:
    def minimumLength(self, s: str) -> int:
        # Two pointers
        left, right = 0, len(s) - 1
        
        # Shrink the string from both ends
        while left < right and s[left] == s[right]:
            char = s[left]
            # Move the left pointer forward while it points to the same character
            while left <= right and s[left] == char:
                left += 1
            # Move the right pointer backward while it points to the same character
            while left <= right and s[right] == char:
                right -= 1
        
        # The remaining string's length
        return right - left + 1




        
        