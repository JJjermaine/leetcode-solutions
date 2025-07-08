# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # perform bfs to calculate sum for each level and append it to array
        # sort the array and return the kth largest
        arr = []
        queue = deque([root])

        # bfs
        while len(queue) > 0:
            count = 0
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                count += node.val

            arr.append(count)

        arr.sort()
        return arr[-k] if k <= len(arr) else -1
        