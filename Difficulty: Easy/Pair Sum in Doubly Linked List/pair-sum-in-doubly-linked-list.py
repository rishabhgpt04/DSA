from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        ptr1 = head 
        ptr2=head
        ans = []
        while(ptr2.next):
            ptr2=ptr2.next
        while(ptr1.data<ptr2.data):
            num1 = ptr1.data
            num2 = ptr2.data
            if num1+num2 > target:
                ptr2=ptr2.prev
            elif num1+num2 < target:
                ptr1=ptr1.next
            else:
                ans.append((ptr1.data, ptr2.data))
                ptr1=ptr1.next
                ptr2=ptr2.prev
        return ans
