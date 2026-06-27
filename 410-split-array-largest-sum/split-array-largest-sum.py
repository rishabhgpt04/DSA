class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        # the answer is bounded by low and high low = max(Arr) and high = sum of the subarray
        sum_arr= sum(nums)
        low = max(nums)
        high = sum_arr
        def chk(mid):
            temp = 1 
            s=0
            for i in range(size):
                if (s+nums[i] <= mid):
                    s+=nums[i]
                else:
                    s=nums[i]
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