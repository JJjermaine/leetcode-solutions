# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        l = dummy
        r = dummy

        for i in range(n):
            r = r.next

        while r.next:
            r = r.next
            l = l.next

        # left.next is the node to be removed
        l.next = l.next.next

        return dummy.next