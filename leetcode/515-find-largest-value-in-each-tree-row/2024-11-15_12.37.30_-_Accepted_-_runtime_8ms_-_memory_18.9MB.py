# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # bfs, keep array for each row and get max for each array
        queue = [(root, 0)]
        level_max = {}

        while queue:
            node, level = queue.pop(0)
            if node:
                if level not in level_max:
                    level_max[level] = node.val
                else:
                    level_max[level] = max(level_max[level], node.val)

                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))

        return [level_max[level] for level in sorted(level_max.keys())]


        