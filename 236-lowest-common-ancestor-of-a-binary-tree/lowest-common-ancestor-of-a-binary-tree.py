# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # without space 
        def dfs(root,p,q):
            if root == None :
                return None
            if root == p or root == q:
                return root
            lans = dfs(root.left,p,q)
            rans = dfs(root.right,p,q)
            if lans and rans:
                return root
            if lans:
                return lans
            if rans:
                return rans
            return None
        return dfs(root,p,q)
