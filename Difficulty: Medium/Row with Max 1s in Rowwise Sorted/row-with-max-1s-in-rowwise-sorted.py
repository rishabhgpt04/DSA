class Solution:
    def rowWithMax1s(self, arr):
        # code here
        rows=len(arr)
        cols = len(arr[0])
        
        
        
        final_ans =0
        ans_ans=-1
        for i in range(rows):
            low = 0
            high= cols-1
            ans =-1
            while(low <=high):
                mid = low + (high-low)//2
                if arr[i][mid]==0:
                    # print(mid)
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if (cols-1-ans > final_ans):
                final_ans = cols-1-ans
                ans_ans = i
            
        return ans_ans