class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        even_count = 0
        odd_exists = False

        # we want to get all even values in the dictionary 
        # and for each odd count we get the even amount of
        #  values to make the longest palindrome
        for key, value in count.items():
            if value % 2 == 0:
                even_count += value
            else: 
                even_count += value - 1
                odd_exists = True

        if odd_exists:
            even_count += 1


        return (even_count)

        