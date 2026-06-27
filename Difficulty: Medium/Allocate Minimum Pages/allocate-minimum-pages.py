class Solution:
    def findPages(self, arr, k):
        # code here
        size = len(arr)
        if size < k:
            return -1
        # arr.sort()
        mx = max(arr)
        sum_arr= sum(arr)
        low = mx
        high= sum_arr
        ans=float('inf')
        def chk(mid):
            # print(mid)
            # take care of each student receives atleast one book 
            s=0
            temp=1
            for i in range(size):
                
                s+=arr[i]
                if s > mid :
                    s = arr[i]
                    temp += 1
                
                if temp > k:
                    return (False,0)
            # print(mid,temp)
            return (True,k)
            
            
        while(low<=high):
            mid = low + (high-low)//2
            res,val=chk(mid)
            if res:
                high=mid-1
                if val ==k:
                    ans = mid
            else:
                low = mid + 1
            
        return -1 if ans == float('inf') else ans
                
            