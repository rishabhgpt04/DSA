class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        size = len(position)
        position.sort()
        low = 1
        high = position[size-1]
        ans = 0
        def chk(mid):
            last_placed = 0
            temp=m-1
            # print(mid)
            for i in range(1,size):
                if (position[i]-position[last_placed]) >= mid :
                    temp-=1
                    last_placed=i
                if temp==0:
                    return True
            return False
        while(low<=high):
            mid = low + (high-low)//2
            if chk(mid):
                ans = mid 
                low = mid + 1
            else:
                high= mid -1 
        return ans
        