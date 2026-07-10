# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        def findMiddle(head):
            """
            one ptr before the middle
            """
            if head==None or head.next==None:
                return head
            fast = head.next  # this is a good techinique remember this **
            slow = head 
            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            return slow
        def merge(list1,list2):
            dummy = ListNode()
            cur = dummy
            temp1=list1 
            temp2 = list2
            while(temp1 and temp2):
                
                if temp1.val<temp2.val:
                    cur.next = temp1
                    temp1=temp1.next
                else:
                    cur.next = temp2
                    temp2= temp2.next
                cur = cur.next
            
            # print(cur.val)
            if temp1:
                cur.next = temp1
            if temp2:
                # print(temp2.val)
                cur.next = temp2
            return dummy.next

        def mergeSort(head):
            if head==None or head.next == None:
                return head
            mid = findMiddle(head)
            leftHead= mergeSort(mid.next)
            mid.next=None
            rightHead=mergeSort(head)
            return merge(leftHead,rightHead)
        return mergeSort(head)
            