# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # split into subtree to find optimal path 
        # dfs
        self.res = float('-inf')

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with split
            self.res = max(self.res, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.res
            

        