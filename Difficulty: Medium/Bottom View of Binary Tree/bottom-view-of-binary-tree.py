'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        mp= {}
        def helper(root,r,c):
            if root == None:
                return 
            if c not in mp:
                mp[c]= (root.data,r)
            else:
                if mp[c][1] <= r:
                    mp[c]=(root.data,r)
            helper(root.left,r+1,c-1)
            helper(root.right,r+1,c+1)
        helper(root,0,0)
        ans = []
        for key,val in sorted(mp.items()):
            ans.append(val[0])
        return ans