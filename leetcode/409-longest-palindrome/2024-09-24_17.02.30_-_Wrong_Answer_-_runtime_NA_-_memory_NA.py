class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        even_count = 0
        largest_odd_count = 0

        # we want to get all even values in the dictionary and the largest count of odd values to make the longest palindrome
        for key, value in count.items():
            if value % 2 == 0:
                even_count += value

            
            if value % 2 != 0:
                largest_odd_count = max(largest_odd_count, value)


        return (even_count + largest_odd_count)

        