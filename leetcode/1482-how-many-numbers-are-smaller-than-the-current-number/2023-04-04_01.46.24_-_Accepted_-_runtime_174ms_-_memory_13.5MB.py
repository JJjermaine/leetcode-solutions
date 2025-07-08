class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        a = []
        for i in nums:
            for j in nums:
                if j < i:
                    count +=1
            a.append(count)
            count = 0
        return a