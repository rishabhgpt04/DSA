# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q= deque()
        
        q.append(root)
        
        ans = []
        flag =False
        while q:
            q1=deque()
            temp = []
        
            while q:
                ele=q.popleft()
                temp.append(ele.val)
                if ele.left:
                    q1.append(ele.left)
                if ele.right:
                    q1.append(ele.right)
            
            q=q1
            if flag:
                ans.append(temp[::-1])
                
            else:
                ans.append(temp)
            flag=not flag
        return ans


         


