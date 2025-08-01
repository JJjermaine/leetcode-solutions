# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        stack = [(cloned)]
        while stack:
            n = stack.pop()
            if n.val == target.val: return n
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)