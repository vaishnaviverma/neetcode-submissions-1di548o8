"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev_new = Node(0)
        pointer = prev_new
        curr = head
        data = {}
        data[None] = None
        while curr:
            curr_new = Node(curr.val, curr.next, None)
            prev_new.next = curr_new
            data[curr] = curr_new
            curr = curr.next
            prev_new = prev_new.next

        curr = head
        curr_new = pointer.next
        while curr and curr_new:
            curr_new.random = data[curr.random]
            curr = curr.next
            curr_new = curr_new.next

        return pointer.next

