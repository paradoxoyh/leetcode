class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==0:
            return 0
        L=[0]*len(nums)
        S=[0]*len(nums)
        L[0]=nums[0]
        S[0]=nums[0]
        res=nums[0]
        for i in xrange(1,len(nums)):
            L[i]=max(L[i-1]*nums[i],S[i-1]*nums[i],nums[i])
            S[i]=min(L[i-1]*nums[i],S[i-1]*nums[i],nums[i])
            res=max(res,L[i])
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        #考虑到是乘法，所以需要将最大值和最小值都保存下来(可能遇见负数)