# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first=head
        def helper(head):
            nonlocal first
            if head == None or head.next ==None:
                return (head,True)
            last , chk= helper(head.next)
            if last.val != first.val:
                chk = False
            first = first.next 
            return (head,chk)
        _,res=helper(head)
        return res