# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head , tail):
            if head is None or head.next is None or head==tail:
                return head
            newHead = reverse(head.next,tail)
            head.next.next = head
            head.next = None 
            return newHead
        if k==1:
            return head
        newHead=None
        cur = head
        groupPrev=None
        while(cur and cur.next):
            temp=k
            head1=cur
            prev=None
            while(temp>0 and cur):
                prev=cur
                cur = cur.next
                temp-=1
            if temp==0:
                nH = reverse(head1, prev)
                if newHead is None:
                    newHead = nH
                if groupPrev:
                    groupPrev.next = nH
                    groupPrev=head1
                else:
                    groupPrev=head1
                head1.next = cur
            else:
                break
        return newHead