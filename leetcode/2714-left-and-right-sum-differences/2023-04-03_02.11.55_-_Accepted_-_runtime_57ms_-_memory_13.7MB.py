class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [] # leftsum
        b = [] # rightsum
        r = nums[::-1] 
        x = 0
        y = 0
        a.append(0)
        b.append(0)
        for i in range(len(nums)-1):
            x += nums[i]
            y += r[i]
            a.append(x)
            b.append(y)
        b = b[::-1]
        for i in range(len(a)):
            a[i] -= b[i] # turn leftsum into difference
            a[i] = abs(a[i])
        return a