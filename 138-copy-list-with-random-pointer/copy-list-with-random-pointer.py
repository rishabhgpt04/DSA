"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        eq= {None:None}
        temp=head
        newHead = Node(0)
        cur = newHead
        
        while(temp):
            x = Node(temp.val)
            # print(x.val)
            # return
            cur.next = x
            
            eq[temp]=x
            temp = temp.next
            cur=cur.next
        # return 
        temp = head

        while(temp):
            # print(eq[temp].val)
            
            eq[temp].random=eq[temp.random]
            temp=temp.next
        return newHead.next

        
            