class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            if (i % 2 == 0):
                a.append(i)
        for i in nums:
            if (i % 2 != 0):
                a.append(i)
        
        return a
