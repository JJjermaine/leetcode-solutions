class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = []
        while num != 0:
            a.append(num % 10) # appends last digit
            num = num // 10 # deletes last digit
        
        a.sort() # sorts from [lowest, highest]
        res = (a[0] * 10 + a[2]) + (a[1] * 10 + a[3]) # [low, high] + [low, high]
        return res

                
