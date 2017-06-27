class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        Set=set(nums)
        res=1
        while Set:
            Max=max(Set)
            temp=Max
            while temp in Set:
                Set.remove(temp)
                temp-=1
            res=max(res,Max-temp)
        return res        
        """
        :type nums: List[int]
        :rtype: int
        """
        