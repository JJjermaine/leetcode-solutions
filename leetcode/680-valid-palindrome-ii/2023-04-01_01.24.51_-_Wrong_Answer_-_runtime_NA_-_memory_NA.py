class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in range(len(s)): # convert given string to only all lowercase alphabets. NOT NEEDED B/C CONSTRINT
            if (s[i].isalnum()): 
                a.append(s[i].lower())
        front = 0
        back = len(a) - 1
        valid = True
        count = 0
        for i in range(len(a)):
            if (len(s) <= 3) and (count > 0) and (len(s) % 2 != 0): # case for odd string bigger than 3
                valid = False
                break
            elif (count > 1): # case for even string
                valid = False
                break

            if front >= back: 
                valid = True
                break

            if (a[front] == a[back]):
                front += 1
                back -= 1
            else: 
                count += 1
                front += 1
                back -= 1
        return valid