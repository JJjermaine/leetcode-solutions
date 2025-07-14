# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = ""

        while head:
            res += str(head.val)
            head = head.next
        
        decimal = 0
        power = 0
        for digit in reversed(res):
            if digit == "1":
                decimal += 2 ** power
            power += 1
        return decimal
        