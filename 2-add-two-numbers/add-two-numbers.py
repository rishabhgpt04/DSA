# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1,l2,carry):
            if l1 is None and l2 is None:
                # temp = l1.val + l2.val +carry
                # newNode = ListNode(temp % 10)
                # carry = temp//10
                
                if carry :
                    newNode=ListNode(0)
                    newNode.val=carry
                    newNode.next =None
                    return newNode
                else :
                    return None

            if l1 is None:
                newNode= ListNode((l2.val+carry)%10)
                carry = (l2.val+carry)//10
                newNode.next=helper(l1,l2.next,carry)
                return newNode
            if l2 is None:
                newNode= ListNode((l1.val+carry)%10)
                carry = (l1.val+carry)//10
                # print(carry)
                newNode.next=helper(l1.next,l2,carry)
                return newNode
            newNode = ListNode(l1.val+l2.val)
            temp = newNode.val + carry
            newNode.val =( newNode.val + carry )%10
            carry = temp // 10 
            newNode.next = helper(l1.next,l2.next,carry)

            # print(carry,head.data)
            return newNode
        head = helper(l1,l2,0)
        return head