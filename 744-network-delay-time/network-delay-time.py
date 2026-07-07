from heapq import heappush , heappop
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n+1)]
        # size = len(times)
        for u,v , time in times :
            adj[u].append((v,time))
        pq=[]
        heappush(pq,(0,k))
        time_taken = [float('inf') ] * (n+1)
        # print(time_taken)
        time_taken[k]=0
        while pq:
            time, node = heappop(pq)
            for nei, wt_time in adj[node]:
                if time_taken[nei] > time + wt_time:
                    time_taken[nei]=time + wt_time
                    heappush(pq,(time + wt_time, nei))
        ans =0
        for i in range(1,n+1):
            if time_taken[i]==float('inf'):
                return -1
            ans = max(ans , time_taken[i])
        return ans