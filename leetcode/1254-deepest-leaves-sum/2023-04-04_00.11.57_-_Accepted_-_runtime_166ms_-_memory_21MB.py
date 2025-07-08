# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr = [root]
        while curr:
            prev = curr
            current = []
            for p in curr:
                for child in [p.left, p.right] :
                    if child:
                        current.append(child)
            curr = current
        return sum(node.val for node in prev)