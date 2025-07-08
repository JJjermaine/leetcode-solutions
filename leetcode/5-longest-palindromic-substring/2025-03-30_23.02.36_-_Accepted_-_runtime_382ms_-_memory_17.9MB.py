class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = 0
        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1

            # Check for even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        return longest

