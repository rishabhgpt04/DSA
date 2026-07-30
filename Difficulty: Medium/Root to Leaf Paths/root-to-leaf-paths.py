"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def paths(self, root):
        # code here
        self.ans = []
        def dfs(root,temp):
            if root == None:
                return 
            if root.left == None and root.right == None :
                temp.append(root.data)
                self.ans.append(temp[:])
                temp.pop()
                return 
            temp.append(root.data)
            dfs(root.left,temp)
            
            dfs(root.right,temp)
            temp.pop()
        temp=[]
        dfs(root,temp)
        return self.ans
                