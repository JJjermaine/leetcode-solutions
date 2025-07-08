class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = []
        while n != 0:
            a.append(n%10)
            n //= 10
        a = a[::-1]
        product = a[0]
        sum = a[0]
        for i in range(len(a)-1):
            product *= a[i+1]
            sum += a[i+1]
        return product - sum 