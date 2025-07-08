# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        prevNode = head
        nextNode = prevNode.next
        
        while(prevNode!=None and nextNode!=None):
            
            newNode = ListNode(math.gcd(prevNode.val, nextNode.val))
            
            prevNode.next = newNode
            newNode.next = nextNode
            
            prevNode = nextNode
            nextNode = prevNode.next
            
        return head