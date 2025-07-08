class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            a.append(i)
        for i in nums:
            a.append(i)
        return a