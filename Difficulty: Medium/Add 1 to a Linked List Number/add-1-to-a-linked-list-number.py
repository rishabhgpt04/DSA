''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        # code here
        def helper(head):
            if head is None:
                return 1
            if head.next is None:
                temp= head.data
                head.data = (head.data+1) % 10
                return (temp + 1)//10
            
            carry = helper(head.next)
            # print(carry,head.data)
            temp= head.data
            head.data = (head.data + carry) % 10
            return (temp + carry)//10
        carry = helper(head)
        
        if carry:
            newNode = Node(carry)
            newNode.next=head
            head=newNode
        return head
            
            