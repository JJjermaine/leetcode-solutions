# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        head = head.next
        curr_sum = 0
        while head:
            if head.val == 0:
                # Create a new node with the sum and attach it to the result
                current.next = ListNode(curr_sum)
                current = current.next
                curr_sum = 0  # Reset the sum for the next segment
            else:
                curr_sum += head.val
            head = head.next  # Move to the next node
        
        return dummy.next  # Return the head of the result linked list
        