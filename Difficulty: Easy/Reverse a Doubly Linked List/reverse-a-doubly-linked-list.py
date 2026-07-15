"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if head is None or head.next is None:
            return head
        temp=head
        last=None
        while(temp):
            last = temp.prev
            temp.prev=temp.next
            temp.next=last
            temp=temp.prev
        return last.prev
        