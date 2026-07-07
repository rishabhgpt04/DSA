# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # delete a cell, 
        def helper(node):
            if node==None or node.next == None:
                return True
            node.val=node.next.val
            chk=helper(node.next)
            if chk:
                node.next=None
            return False
        helper(node) 
        