'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        # 3 new listNodes for each 
        ptr0 = Node(-1)
        ptr1 = Node(-1)
        ptr2 = Node(-1)
        temp0=ptr0
        temp1=ptr1
        temp2=ptr2
        cur =head
        while(cur ):
            if cur.data== 0:
                temp0.next = cur
                temp0= temp0.next
            if cur.data== 1:
                temp1.next = cur
                temp1= temp1.next
            if cur.data== 2:
                temp2.next = cur
                temp2= temp2.next
            cur = cur.next
        temp0.next=ptr1.next if ptr1.next else ptr2.next
        temp1.next=ptr2.next
        temp2.next=None
        return ptr0.next
            
        