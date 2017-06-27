class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return '0'
        for i in xrange(len(nums)):
            nums[i]=str(nums[i])
        ret=[nums[0]]
        nums.pop(0)
        while nums:
            i=0
            while i < len(ret):
                if int(ret[i]+nums[0])<=int(nums[0]+ret[i]):
                    ret.insert(i,nums[0])
                    nums.pop(0)
                    break
                i+=1
            else:
                ret.append(nums[0])
                nums.pop(0)
        return str(int(''.join(ret)))