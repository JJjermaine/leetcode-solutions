class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if deleting the left character makes the rest of the string a palindrome
                if self.isPalindrome(s, left + 1, right):
                    return True
                # Check if deleting the right character makes the rest of the string a palindrome
                elif self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    # Both substrings are not palindromes
                    return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True