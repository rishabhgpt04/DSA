# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        cur = headRef
        last = None
        while(cur and cur.next):
            last=cur
            # print(cur.data)
            while cur.next and  cur.data == cur.next.data:
                cur=cur.next
            if last!=cur:
                last.next=cur.next
                # print(last.data,cur.data)
                if cur.next :
                    cur.next.prev = last
                    continue
            cur = cur.next
        return headRef