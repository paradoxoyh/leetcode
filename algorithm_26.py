class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=1:
            return len(nums)
        i=1
        while len(nums)>i:
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
