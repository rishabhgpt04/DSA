class Solution:
    def median(self, mat):
        # code here

        rows = len(mat)
        cols = len(mat[0])
        size = rows * cols

        def upper_bound(arr, x):
            low = 0
            high = len(arr) - 1
            ans = len(arr)

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] > x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        mn = float('inf')
        mx = float('-inf')

        for i in range(rows):
            mn = min(mn, mat[i][0])
            mx = max(mx, mat[i][cols - 1])

        low = mn
        high = mx

        def chk(mid):
            res = 0
            for i in range(rows):
                res += upper_bound(mat[i], mid)
            return res

        while low <= high:
            mid = low + (high - low) // 2
            count = chk(mid)

            if count <= (size // 2):
                low = mid +1 
            
            else:
                high = mid - 1

        return low