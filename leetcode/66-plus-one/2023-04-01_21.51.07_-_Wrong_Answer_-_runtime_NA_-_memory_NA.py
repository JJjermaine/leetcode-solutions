class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = []
        back = len(digits) - 1
        digits[back] += 1
        string = ""
        for i in digits:
            string += str(i) 
        for i in string:
            a.append(int(i))
        return a
