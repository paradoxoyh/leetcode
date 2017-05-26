class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i]==i+1:
                pass
            else:
                x=nums[i]
                while x>0 and x<=len(nums) and x!=nums[x-1]:
                    nums[x-1],x=x,nums[x-1]
                    #x,nums[x-1]=nums[x-1],x
        for i in xrange(len(nums)):
            if i+1!=nums[i]:
                return i+1
                break
        return len(nums)+1
        """
        :type nums: List[int]
        :rtype: int
        """
        #交换顺序会出现问题？？？
        
