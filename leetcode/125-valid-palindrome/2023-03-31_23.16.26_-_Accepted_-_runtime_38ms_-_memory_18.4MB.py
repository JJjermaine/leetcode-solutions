class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in range(len(s)):
            if (s[i].isalnum()):
                a.append(s[i].lower())
        front = 0
        back = len(a) - 1
        valid = True
        for i in range(len(a)):
            if front == back:
                valid = True
            if (a[front] == a[back]):
                front += 1
                back -= 1
            else: 
                valid = False
        return valid

            