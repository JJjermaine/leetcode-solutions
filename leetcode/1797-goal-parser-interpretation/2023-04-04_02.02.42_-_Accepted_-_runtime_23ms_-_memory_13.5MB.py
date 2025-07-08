class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        a = command
        a = a.replace('()','o')
        a = a.replace('(al)','al')
        return a