# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        nums=[]
        ret=[]
        for i in intervals:
            nums.append(i.start)
        temp=nums
        nums=sorted(nums)
        for i in range(len(nums)):
            Index=temp.index(nums[i])
            ret.append(intervals[Index])
            temp.pop(Index)
            intervals.pop(Index)
        i=0
        while i<len(ret)-1:
            if ret[i].end>=ret[i+1].start:
                if ret[i].end<=ret[i+1].end:
                    ret[i].end=ret[i+1].end
                ret.pop(i+1)
            else:
                i+=1
        return ret
                    
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
