# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l,r):
            if l == None and r == None:
                return True
            if l==None or r==None:
                return False
            flag1=helper(l.left,r.right)
            flag2=helper(l.right, r.left)
            return flag1 and flag2 and l.val==r.val
        return helper(root,root)