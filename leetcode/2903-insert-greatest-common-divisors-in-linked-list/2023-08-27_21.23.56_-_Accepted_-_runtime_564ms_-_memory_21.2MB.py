# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            result = min(a, b)
            while result:
                if a % result == 0 and b % result == 0:
                    break
                result -= 1
        
            return result
        
        curr = head

        while curr is not None and curr.next is not None:
            curr.next = ListNode(gcd(curr.val, curr.next.val), next=curr.next)
            curr = curr.next.next

        return head