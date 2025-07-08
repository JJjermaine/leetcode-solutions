class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = []
        while num != 0:
            l.append(num % 10) # appends last digit
            num = num // 10 # deletes last digit
        
        l.sort() # sorts from [lowest, highest]
        res = (l[0] * 10 + l[2]) + (l[1] * 10 + l[3]) # [low, high] + [low, high]
        return res

                
