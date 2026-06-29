from heapq import heappush,heappop
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0]==1:
            return -1
        pq = []
        # initial configuration - 
        heappush(pq,(1,0,0))
        dist_arr = [[float('inf') ] * cols for _ in range(rows)]
        dist_arr[0][0]=1
        dirs=[(0,1), (0,-1) , (1,0) ,(-1,0) , (-1,-1) , (-1,1) , (1,-1), (1,1)]
        while pq :
            dist,row,col= heappop(pq)
            if (row==rows-1 and col==cols-1):
                return dist
            for dx ,dy in dirs:
                nrow= row+dx
                ncol = col + dy
                if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and grid[nrow][ncol]==0:
                    if dist_arr[nrow][ncol] > 1+dist:
                        dist_arr[nrow][ncol]= 1+dist
                        ndist=1+dist
                        heappush(pq,(ndist,nrow,ncol))
        return -1
        
        