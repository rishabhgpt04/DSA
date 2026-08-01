# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        cnt = 1
        q= deque([(root,1)])
        while q:
            lvl=[]
            # print("length", len(q))
            for _ in range(len(q)):
                
                node,idx = q.popleft()
                # print(node.val)
                lvl.append((node.val,idx))
                
                if node.left:
                   
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right,2*idx+1))
                    
            # print(lvl)
            self.ans = max(self.ans ,lvl[-1][1] - lvl[0][1]  + 1)
        return self.ans