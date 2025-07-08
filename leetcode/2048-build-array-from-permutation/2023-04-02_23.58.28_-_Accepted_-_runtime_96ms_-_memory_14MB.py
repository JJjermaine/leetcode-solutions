class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)):
            a.append(nums[nums[i]])
        return a
