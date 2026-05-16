# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansl = ListNode()
        pointer = ansl
        p1, p2 = l1, l2
        csum = 0
        carry = 0

        while p1 and p2:
            csum = p1.val + p2.val + carry 
            carry = int(csum/10)
            csum = csum%10
            newnode = ListNode(csum)
            ansl.next = newnode
            ansl = ansl.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            csum = p1.val + carry
            carry = int(csum/10)
            csum = csum%10
            newnode = ListNode(csum)
            ansl.next = newnode
            ansl = ansl.next
            p1 = p1.next

        while p2:
            csum = p2.val + carry
            carry = int(csum/10)
            csum = csum%10
            newnode = ListNode(csum)
            ansl.next = newnode
            ansl = ansl.next
            p2 = p2.next

        if carry != 0:
            newnode = ListNode(carry)
            ansl.next = newnode
        return pointer.next

        

        