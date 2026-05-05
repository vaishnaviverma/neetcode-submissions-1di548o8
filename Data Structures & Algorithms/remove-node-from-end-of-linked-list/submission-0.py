# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l = 0
        while curr:
            l+=1
            curr=curr.next
        reql = l-n+1
        curr=head
        l=1
        past = None
        if reql==1:
            return head.next
        while l<=reql:
            if l==reql:
                past.next=past.next.next
                return head
            past=curr
            curr=curr.next
            l+=1