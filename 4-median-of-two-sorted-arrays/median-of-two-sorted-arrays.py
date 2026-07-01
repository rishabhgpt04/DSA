class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        size = size1+size2
        req= size//2
        prev,cur=0,0
        i,j=0,0
        while(i+j<req+1):
            prev=cur
            if i<size1 and (j>=size2 or  nums1[i] < nums2[j]):
                cur = nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        if size % 2 ==0:
            return (prev+cur)/2.0
        return float(cur)


        
