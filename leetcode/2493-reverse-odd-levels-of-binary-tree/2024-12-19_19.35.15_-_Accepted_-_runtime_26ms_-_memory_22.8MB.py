# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(leftChild, rightChild, level):
            if not leftChild: #perfect binary tree so no need to check right
                return
            if level % 2 == 0: # if odd level, swap
                leftChild.val, rightChild.val = rightChild.val, leftChild.val

            DFS(leftChild.left, rightChild.right, level + 1)
            DFS(leftChild.right, rightChild.left, level + 1)

        DFS(root.left, root.right, 0)
        return root
        