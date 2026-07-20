class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=[[float('inf')] *n for _ in range(n)]
        for u,v,wt in edges:
            adj[u][v]=wt
            adj[v][u]=wt
        for i in range(n):
            adj[i][i]=0
        print(adj)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j]= min(adj[i][j],  adj[i][k] + adj[k][j])
        min_city=float('inf')
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(n):
                if adj[i][j] <= distanceThreshold:
                    cnt+=1
            if cnt <= min_city:
                min_city= cnt 
                ans = i
        return ans
            
            