# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        # dfs on the right
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)

        dfs(root)
        return root