class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        for i in xrange(0,len(nums)):
            if i>0 and i<len(nums)-1:
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    return i
                    break
            elif i==0 and nums[i]>nums[i+1]:
                return i
                break
            elif i==len(nums)-1 and nums[i]>nums[i-1]:
                return i
                break
                
        """
        :type nums: List[int]
        :rtype: int
        """
        