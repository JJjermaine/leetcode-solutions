import numpy as np
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        for i in nums:
            if (i % 2 == 0):
                a.append(i)
            if (i % 2 != 0):
                b.append(i)
        
        c = np.concatenate((a, b))

        return c
