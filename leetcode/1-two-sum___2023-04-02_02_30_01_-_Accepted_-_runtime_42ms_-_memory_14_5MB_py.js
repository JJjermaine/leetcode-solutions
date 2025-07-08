class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[value] = index