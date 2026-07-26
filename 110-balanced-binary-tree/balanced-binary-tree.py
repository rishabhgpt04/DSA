# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root == None :
                return 0
            if  (root.left == None and root.right==None):
                return 1
            leftHeight= helper(root.left)
            rightHeight= helper(root.right)
            if leftHeight==-1 or rightHeight==-1:
                return -1
            if abs(leftHeight-rightHeight)>1:
                return -1
            return 1+max(leftHeight,rightHeight)
        if helper(root)!=-1:
            return True
        return False