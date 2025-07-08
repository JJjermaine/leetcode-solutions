class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for i in accounts:
            if max < sum(i):
                max = sum(i)
        return max
