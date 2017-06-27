class Solution(object):
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        num=list(s)
        link=[0 for j in range(1+len(num))]
        if num[0]!='0':
            link[0]=1
        for i in range(len(num)):
            if num[i]!='0':
                link[i+1]+=link[i]
            if 10<=int(num[i-1]+num[i])<=26 and i-1>=0:
                link[i+1]+=link[i-1]
        return link[i+1]
        """
        :type s: str
        :rtype: int
        """
        