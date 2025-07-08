# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # create a copy of the reversed version
        # iterate original and copy un until half way
        # step 1: create a reverse version of current linked list
        new_head = None
        curr = head

        while curr:
            new_node = ListNode(curr.val)
            new_node.next = new_head
            new_head = new_node
            curr = curr.next

        # Step 2: Traverse both lists until halfway
        max_sum = 0
        slow = head
        fast = head
        steps = 0

        # count number of nodes to go half way
        while fast and fast.next:
            steps += 1
            fast = fast.next.next


        # iterate through original and reversed version
        rev = new_head # reset new_head
        for _ in range(steps):
            max_sum = max(max_sum, slow.val + rev.val)
            slow = slow.next
            rev = rev.next
        
        return max_sum