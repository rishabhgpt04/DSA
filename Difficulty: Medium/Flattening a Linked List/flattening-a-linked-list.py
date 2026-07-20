'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
from heapq import heappush,heappop
class Solution:
    def flatten(self, root):
        # code here
        if root is None or root.next is None:
            return root
        temp = root
        pq=[]
        unique_id = 0
        while(temp):
            # print(temp.data)
            heappush(pq,(temp.data,unique_id, temp))
            unique_id +=1
            temp=temp.next
        head = Node(0)
        temp_head = head
        while pq:
            _,_,temp = heappop(pq)
            temp_head.bottom = temp
            if temp.bottom:
                heappush(pq,(temp.bottom.data ,unique_id, temp.bottom))
                unique_id+=1
            temp_head=temp_head.bottom
        return head.bottom