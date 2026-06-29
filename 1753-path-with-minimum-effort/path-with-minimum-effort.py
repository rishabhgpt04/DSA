from heapq import heappush,heappop
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])
        
        dist_arr = [[float('inf') ] * cols  for _ in range(rows)]

        pq=[]
        dist_arr[0][0]=0
        heappush(pq,(0,0,0))
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while pq:
            dist,row,col=heappop(pq)
            if row == rows-1 and col == cols-1:
                return dist
            for dx,dy in dirs:
                nrow= dx + row
                ncol = dy + col
                if nrow >=0 and nrow < rows and ncol >=0 and ncol <cols :
                    ndist = max(dist , abs(heights[row][col] - heights[nrow][ncol]))
                    if dist_arr[nrow][ncol] > ndist:
                        # print(nrow,ncol,ndist)
                        dist_arr[nrow][ncol]=ndist
                        heappush(pq,(ndist, nrow,ncol))
        return -1
            