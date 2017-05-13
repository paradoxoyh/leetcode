class Solution(object):
    def reverse(self, x):
        tag=1
        if x<0:
            tag=-1
            x=abs(x)
        ret=0
        while x>=10:
            temp=x%10
            x=int(x/10)
            ret=ret*10+temp
        ret=ret*10+x
        if tag==-1:
            ret=-ret
        if ret >= 2147483647 or ret <= -2147483648:
            return 0
        return ret
        """
        :type x: int
        :rtype: int
        """
        