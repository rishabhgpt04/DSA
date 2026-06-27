class Solution:
    def minTime (self, arr, k):
        # code here
         # same as split 
        size = len(arr)
        # the answer is bounded by low and high low = max(Arr) and high = sum of the subarray
        sum_arr= sum(arr)
        low = max(arr)
        high = sum_arr
        def chk(mid):
            temp = 1 
            s=0
            for i in range(size):
                if (s+arr[i] <= mid):
                    s+=arr[i]
                else:
                    s=arr[i]
                    temp+=1
            return temp
        ans = float('inf')
        while( low <= high):
            mid = low + (high-low)//2
            split = chk(mid)
            if split<=k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
        return ans