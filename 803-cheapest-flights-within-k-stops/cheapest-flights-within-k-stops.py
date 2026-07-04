from heapq import heappush, heappop
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        size = len(flights)
        adj=[[] for _ in range(n)]
        for u,v , wt in flights:
            adj[u].append((v,wt))
        pq=[]
        heappush(pq,(0,src,0))
        dist=[(float('inf'))] * n 
        dist[src]=0
        while pq:
            steps,node, dist_to_reach = heappop(pq)
            # if node == dst:
            #     return dist_to_reach
            if steps>k:
                continue
            for nei,wt in adj[node]:
                # print(node , nei).
                if dist_to_reach + wt < dist[nei]:
                    dist[nei]=dist_to_reach + wt
                    heappush(pq,(steps+1,nei,dist_to_reach + wt))
        # print(dist)
        return dist[dst] if dist[dst]!=float('inf') else -1
        # return -1
