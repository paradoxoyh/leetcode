class Solution(object):
    def threeSum(self, nums):
        ret = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k, j = i+1, len(nums)-1
            while k < j:
                s = nums[i] + nums[k] + nums[j]
                if s < 0:
                    k +=1 
                elif s > 0:
                    j -= 1
                else:
                    ret.append((nums[i], nums[k], nums[j]))
                    while k < j and nums[k] == nums[k+1]:
                        k += 1
                    while k < j and nums[j] == nums[j-1]:
                        j -= 1
                    k += 1; j -= 1
        return ret