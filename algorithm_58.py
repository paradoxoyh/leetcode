class Solution(object):
    def lengthOfLastWord(self, s):
        s,count,last=list(s),0,0
        for i in s:
            if i==' ':
                count=0
            else:
                count+=1
            if count!=0:
                last=count
        return last
        """
        :type s: str
        :rtype: int
        """
        
