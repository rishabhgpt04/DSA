# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root,par,mp,mp_val_node):
            if root == None:
                return
            if root.val not in mp_val_node:
                mp_val_node[root.val]=root  
            mp[root.val]=par
            dfs(root.left,root.val,mp,mp_val_node) 
            dfs(root.right,root.val,mp,mp_val_node)
        mp={}
        mp_val_node={}
        dfs(root,float('inf'),mp,mp_val_node)
        
        temp1 = p.val
        temp2= q.val
        ancesstors= set()
        while(temp1!=float('inf')):
            ancesstors.add(temp1)
            temp1=mp[temp1]
        while temp2 not in ancesstors:
            temp2=mp[temp2]
        return mp_val_node[temp2] 
            