class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        even_count = 0
        odd_count = 0

        # we want to get all even values in the dicotionary and at most one count of odd values to make the longest palindrome
        for key, value in count.items():
            if value % 2 == 0: # is even
                while value:
                    even_count += 2
                    value -= 2
            elif value % 2 != 0 and odd_count < 1:
                odd_count += 1


        return (even_count + odd_count)

        