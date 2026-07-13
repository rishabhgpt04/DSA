# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        while(tempA and tempB):
            tempA=tempA.next
            tempB=tempB.next
        if tempA == None:
            tempA=headA
            tempB2=headB
            while(tempB):
                
                tempB2=tempB2.next
                tempB=tempB.next
            
            print(tempB2.val)
            while(tempA and tempB2  and tempA!=tempB2):
                if tempA.next==None or tempB2.next==None:
                    return None
                tempA=tempA.next
                tempB2=tempB2.next
            return tempB2
        if tempB == None:
            tempB=headB
            tempA2=headA
            
            while(tempA):
                tempA=tempA.next
                tempA2=tempA2.next
            # print(tempA2.val)
            while(tempA2  and tempB and tempA2!=tempB):
                if tempA2.next==None or tempB.next==None:
                    return None
                tempA2=tempA2.next
                tempB=tempB.next
            return tempA2
            
        