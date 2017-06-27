class Solution(object):
    def rotate(self, nums, k):
        l=len(nums)
        k=k%l
        for i in xrange(k):
            nums.insert(0,nums[-1])
            nums.pop()
        #nums=nums[:l]
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        