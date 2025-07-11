# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ans not my own
        # bfs with queue
        # use queue to:
        #   add root to res and pop
        #   add children to queue and repeat

        res = []
        q = deque()
        q.append(root)

        while q:
            qlength = len(q)
            level = []
            for i in range(qlength):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
