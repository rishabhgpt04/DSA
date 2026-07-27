# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf') 
        def helper(root):
            if root is None :
                return 0
            leftPathSum = helper(root.left)
            rightPathSum = helper(root.right)
            self.ans = max(self.ans , leftPathSum+ rightPathSum + root.val, root.val+leftPathSum, root.val+rightPathSum, root.val)
            return root.val + max(leftPathSum , rightPathSum,0)
        helper(root)
        return self.ans