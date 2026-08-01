'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        def dfs(root):
            if root is None:
                return 0
            if root.left == None and root.right==None:
                return root.data
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            if leftSum == -1 or rightSum ==-1 or leftSum+rightSum != root.data:
                return -1
            return root.data
        if dfs(root)==-1:
            return False
        return True
            