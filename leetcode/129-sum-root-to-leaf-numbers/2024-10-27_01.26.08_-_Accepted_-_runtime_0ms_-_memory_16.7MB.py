# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # just perform dfs
        self.res = 0
        def dfs(curr, num):
            if not curr.left and not curr.right:
                self.res += num * 10 + curr.val
                return

            if curr.left:
                dfs(curr.left, num*10 + curr.val)
            if curr.right:
                dfs(curr.right, num*10 + curr.val)

        dfs(root, 0)
        return self.res


        