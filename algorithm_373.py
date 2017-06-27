class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        count=0
        ret=[]
        tar=[]
        temp=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tar.append(nums1[i]+nums2[j])
        if len(tar)==0:
            return ret
        max_num=max(tar)+1
        while count<k and count<len(tar):
            temp=tar.index(min(tar))
            tar[temp]=max_num
            i=temp/len(nums2)
            j=temp%len(nums2)
            ret.append([nums1[i],nums2[j]])
            count+=1
        return ret                
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        