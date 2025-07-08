class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        a = []
        for i in address:
            if (i == '.'):
                a.append("[.]")
            else:
                a.append(i)
        s = ''.join(a)
        return s