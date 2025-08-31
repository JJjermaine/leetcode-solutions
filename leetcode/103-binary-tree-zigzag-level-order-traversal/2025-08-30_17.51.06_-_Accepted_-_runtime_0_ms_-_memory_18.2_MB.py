# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs and rotate each time
        curr = []
        res = []
        self.left2right = True
        def bfs(root):
            if not root:
                return

            queue = deque([root])
            while queue:
                curr = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    curr.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                if self.left2right == True:
                    res.append(curr)
                    self.left2right = False
                else:
                    res.append(curr[::-1])
                    self.left2right = True
        bfs(root)
        return res

