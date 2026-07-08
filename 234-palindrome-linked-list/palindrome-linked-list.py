# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if head == None or head.next == None :
                return head
            newHead = reverse(head.next)
            head.next.next = head
            head.next = None
            return newHead
        slow = head
        fast=head
        while(fast and fast.next):
            slow = slow.next
            fast=fast.next.next
        rev_head=reverse(slow)
        print(head.val)
        print(rev_head.val)
        while(rev_head):
            if head.val!=rev_head.val:
                return False
            head=head.next
            rev_head=rev_head.next
        return True