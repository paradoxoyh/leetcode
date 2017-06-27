class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=0,0
        while i<m or j<n:
            if j==n:
                nums1.append(nums1[0])
                nums1.pop(0)
                i+=1
            elif i==m:
                nums1.append(nums2[0])
                nums2.pop(0)
                j+=1
            elif nums1[0]>=nums2[0]:
                nums1.append(nums2[0])
                nums2.pop(0)
                j+=1
            elif nums1[0]<=nums2[0]:
                nums1.append(nums1[0])
                nums1.pop(0)
                i+=1
        for j in xrange(n):
            nums1.pop(0)
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """