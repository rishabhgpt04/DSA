"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        def remove_key(temp):
            # print(temp.data)
            nonlocal head
            last=temp.prev
            
            if last:
                last.next=temp.next
            else:
                head=temp.next
            if temp.next:
                
                temp.next.prev=temp.prev
            temp.next=None
            temp.prev=None
        cur=head
        while(cur):
            
            if cur.data==x:
                
                temp=cur
                cur=cur.next
                
                remove_key(temp)
                
            else:
                cur=cur.next
        
        return head
            