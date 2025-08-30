# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # since we do not know the length of the linked lists, go to the end and traverse from there
        # needed help
        # Helper to compute length
        def length(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        n1, n2 = length(l1), length(l2)

        # Pad the shorter list with zeros in front
        while n1 < n2:
            l1 = ListNode(0, l1)
            n1 += 1
        while n2 < n1:
            l2 = ListNode(0, l2)
            n2 += 1

        # Recursive function that returns (carry, node)
        def add_rec(a, b):
            if not a and not b:
                return (0, None)
            
            carry, next_node = add_rec(a.next, b.next)
            total = a.val + b.val + carry
            node = ListNode(total % 10)
            node.next = next_node
            return (total // 10, node)

        carry, head = add_rec(l1, l2)

        # If there's a carry left, add it to the front
        if carry:
            head = ListNode(carry, head)
        
        return head