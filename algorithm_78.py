class Solution(object):
    def subsets(self, nums):
        res = []
        n=len(nums)
        for i in range(n+1):
            self.dfs(nums, i, [], res)
        return res
    def dfs(self, nums, k, path, res):
        if k == 0:
            res.append(path)
            return
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], k-1, path+[nums[i]], res)
        return
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]a
        """
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #对k=0到len(nums)依次调用algorithm77