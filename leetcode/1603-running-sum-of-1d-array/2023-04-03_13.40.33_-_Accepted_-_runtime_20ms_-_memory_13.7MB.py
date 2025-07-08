class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        x = 0
        for i in nums:
            x += i
            a.append(x)
        return a