# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head 
        ptr2 = head 
        while(n):
            ptr1=ptr1.next
            n-=1
        if ptr1==None:
            head=head.next 
            return head
        while(ptr1 and ptr1.next):
            ptr1=ptr1.next
            ptr2=ptr2.next
        
        if ptr2.next.next:
            ptr2.next = ptr2.next.next
        else:
            ptr2.next = None
        return head