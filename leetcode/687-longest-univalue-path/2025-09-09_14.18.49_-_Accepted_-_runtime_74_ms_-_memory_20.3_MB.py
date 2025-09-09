# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Extend paths only if child matches current node’s value
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0

            # Update global maximum with the path that goes THROUGH this node
            self.max = max(self.max, left_path + right_path)

            # Return the longer one to continue upward
            return max(left_path, right_path)

        dfs(root)
        return self.max