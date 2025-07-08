class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        num = 0
        for i in operations:
            if i == "--X" or i == "X--":
                num -= 1
            else:
                num +=1
        return num
