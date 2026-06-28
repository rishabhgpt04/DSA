from heapq import heappush,heappop
class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        # lets do the brute force
        size = len(stations)
        howMany=[0] * size
        pq=[]
        for i in range(1,size):
            diff = (stations[i]-stations[i-1])
            heappush(pq,(-diff,i))
        # print(pq)
        
        for _ in range(k):
            if pq:
                _, ind  = heappop(pq)
                dif= stations[ind]-stations[ind-1]
                howMany[ind]+=1
                newLen = dif*1.0/ (howMany[ind] + 1)
                heappush(pq,(-newLen,ind))
        
        ans = 0
        # print(howMany)
        for i in range(1,size):
            ans = max(ans , (stations[i]- stations[i-1])*1.0/(howMany[i] +1))
        return ans
                