class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) in [1,2]:
            return len(nums)
        p0,p1,p2=0,1,2
        while p2<len(nums):
            if nums[p0]==nums[p1]:
                if nums[p2]==nums[p1]:
                    nums.pop(p0)
                else:
                    p0+=2
                    p1+=2
                    p2+=2
            else:
                p0+=1
                p1+=1
                p2+=1
