class Solution(object):
    def maxSubArray(self, nums):
        leng=len(nums)
        if leng==0:
            return 0
        #Max=nums[0]
        tag=0
        for i in nums:
            if i>=0:
                tag=1
                break
        if tag==0:
            return max(nums)
        Max=0
        Sum=0
        for i in range(leng):
            if Max+nums[i]>0:
                Max=Max+nums[i]
                if Max>Sum:
                    Sum=Max
            elif Max+nums[i]<=0:
                Max=0
        return Sum
        """
        :type nums: List[int]
        :rtype: int
        """
        
