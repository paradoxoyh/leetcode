class Solution(object):
    def sortColors(self, nums):
        red=[]
        white=[]
        blue=[]
        i=0
        count=0
        while count<len(nums):
            if nums[i]==0:
                nums.pop(i)
                nums.insert(0,0)
                i+=1
            elif nums[i]==2:
                nums.pop(i)
                nums.append(2)
            else:
                i+=1
            count+=1
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        