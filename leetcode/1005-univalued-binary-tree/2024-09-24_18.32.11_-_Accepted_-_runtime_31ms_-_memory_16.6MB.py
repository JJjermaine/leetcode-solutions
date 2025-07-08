# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        target = root.val

        def search(root, target):
            if not root:
                return True

            return target == root.val and search(root.left, target) and search(root.right, target)

        return search(root, target)
        