# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head,mem):
            if head is None :
                return None
            if head in mem:
                return head
            mem[head]= True
            chk = helper(head.next,mem)
            return chk
        mem={}
        return helper(head,mem)
        