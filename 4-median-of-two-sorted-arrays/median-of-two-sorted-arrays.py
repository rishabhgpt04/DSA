class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        maxHeap=[] # max heap of smaller nums 
        minHeap=[] # min heap of bigger nums 
        # we try to balance the length of both.
        def addNum(num):
            if not maxHeap or num <= -maxHeap[0]:
                heappush(maxHeap,-num)
            else:
                heappush(minHeap,num)
            # now balance part I am okat with maxHeap being bigger by 1 (odd number of elements)

            if len(maxHeap) > len(minHeap) +1:
                heappush(minHeap, -heappop(maxHeap))
            if len(minHeap) > len(maxHeap):
                heappush(maxHeap, -heappop(minHeap))
        for num in nums1:
            addNum(num)
        for num in nums2:
            addNum(num)
        if len(maxHeap) > len(minHeap):
            return -1.0* maxHeap[0]
        else:
            # print("Hello")
            # print(maxHeap)
            # print(minHeap)
            return (-maxHeap[0] + minHeap[0] )/2.0
