
from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        q=deque()
        q.append((0,start))
        vis = [0] * 1000
        while q:
            moves , num = q.popleft()
            
            if num == end :
                return moves
            if vis[num]==1:
                continue
            vis[num]=1
            for ele in arr:
                newNum = (ele * num ) %1000
                q.append((moves+1, newNum))
        return -1
                