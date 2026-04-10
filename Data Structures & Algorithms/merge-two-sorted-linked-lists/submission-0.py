# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        temp = newhead
        p1 = list1
        p2 = list2
        while p1 and p2:
            newn = ListNode()
            if p1.val<p2.val:
                newn.val=p1.val
                p1=p1.next
            else:
                newn.val=p2.val
                p2=p2.next
            temp.next=newn
            temp=temp.next
        while p1:
            newn = ListNode()
            newn.val=p1.val
            p1=p1.next
            temp.next=newn
            temp=temp.next
        while p2:
            newn = ListNode()
            newn.val=p2.val
            p2=p2.next
            temp.next=newn
            temp=temp.next
        return newhead.next
