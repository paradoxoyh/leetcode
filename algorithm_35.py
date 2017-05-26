class Solution(object):
    def searchInsert(self, nums, target):
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if target<=nums[i]:
                    return i
                    break
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
