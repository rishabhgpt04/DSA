# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 1
        if head is None or head.next is None :
            return head
        sizePtr=head
        while(sizePtr.next):
            sizePtr=sizePtr.next
            size +=1 
        k= k % size 
        temp = head
        if k==0:
            return head
        while(k>=1):
            temp=temp.next
            k-=1
        tempPrev=head
        while(temp.next):
            tempPrev=tempPrev.next
            temp=temp.next
        print(tempPrev.val)
        print(temp.val)
        newHead=None

        if tempPrev.next:
            newHead=tempPrev.next
        tempPrev.next=None
        
        temp.next=head
        return newHead

