'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        mp={}
        def dfs(root,c,r ):
            if root == None:
                return 
            if c not in mp:
                mp[c]=(root.data,r)
            elif(mp[c][1]>r):
                mp[c]=(root.data,r)
            dfs(root.left,c-1,r+1)
            dfs(root.right,c+1,r+1)
        dfs(root,0,0)
        ans = []
        for key,val in sorted(mp.items()):
            # print(key,val)
            ans.append(val[0])
        return ans
        