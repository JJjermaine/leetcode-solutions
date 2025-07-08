# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        NOT_MONITORED = 0
        HAS_CAMERA = 1
        MONITORED = 2

        self.camera_count = 0

        def dfs(node):
            if not node:
                return 

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NOT_MONITORED or right == NOT_MONITORED:
                self.camera_count += 1
                return HAS_CAMERA
            
            if left == HAS_CAMERA or right == HAS_CAMERA:
                return MONITORED

            return NOT_MONITORED

        # If root is not monitored, we need to place a camera at root
        if dfs(root) == NOT_MONITORED:
            self.camera_count += 1

        return self.camera_count