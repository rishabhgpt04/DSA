'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root ):
        # code here
        if root is None:
            return []
        
        ans = []
        ans.append(root.data)
        if root.left==None and root.right==None:
            return ans
        def helper(root):
            if root == None:
                return 
            if root.left == None and root.right == None:
                return 
            ans.append(root.data)
            if root.left:
                helper(root.left)
            else:
                helper(root.right)
        helper(root.left)
        def leaf(root):
            if root==None:
                return
            if root.left == None and root.right == None:
                ans.append(root.data)
            leaf(root.left)
            leaf(root.right)
        leaf(root)
        def right(root):
            if root == None:
                return 
            if root.left == None and root.right == None:
                return
            if root.right:
                right(root.right)
            else:
                right(root.left)
            ans.append(root.data)
        right(root.right)
        # ans.pop()
        return ans 
            
        