# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dp = [[] * 20001 for _ in range(1001)]
        self.minC = 0
        self.maxC = 0
        self.max_r=0
        def dfs(root,c,r):
            if root == None:
                return 
            self.max_r=max(self.max_r,r)
            self.maxC= max(c,self.maxC)
            self.minC= min(c,self.minC)
            dfs(root.left,c-1,r+1)
            dfs(root.right,c+1,r+1)
        dfs(root,0,0)
        l= (self.maxC-self.minC)+1
        dp = [[[] for _ in range(l)] for _ in range(self.max_r + 1)]
        # print(dp)
        def dfs2(root,r,c):
            if root == None:
                return
            print(r,c) 
            
            dp[r][c + abs(self.minC)].append(root.val)
            dfs2(root.left,r+1,c-1)
            dfs2(root.right,r+1,c+1)
        dfs2(root,0,0)
        # print(dp)
        ans =[]
        for j in range(l):
            temp=[]
            for i in range(self.max_r+1):
                if dp[i][j]:
                    temp.extend(sorted(dp[i][j]))
            ans.append(temp)
        return ans