class Solution(object):
    def canJump(self, nums):
        last_local=0
        while 0 in nums:
            local=nums.index(0)
            tag=0
            for i in range(last_local,local+1):
                if local!=len(nums)-1:
                    if nums[i]+i>local:
                        tag=1
                elif nums[i]+i>=local:
                    tag=1
            last=local
            nums[local]=1
            if tag==0:
                return False
                break
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
