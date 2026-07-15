'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        
        # Code Here
        temp=head
        while(p):
            temp=temp.next
            p-=1
        newNode=Node(x)
        newNode.next=temp.next
        newNode.prev=temp
        if temp.next:
            temp.next.prev=newNode
        temp.next=newNode
        
        return head
            