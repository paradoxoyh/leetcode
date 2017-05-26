class Solution(object):
    def myPow(self, x, n):
        return x**n
        ##Time limit exceed
        if n==0:
            return 1
        x0=x
        N=abs(n)
        for i in xrange(N-1):
            x*=x0
        if n>0:
            return x
        else:
            return 1/x
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #可以使用递归或者迭代来进行计算，不会超时
        #迭代：n>>1,O(log(n))
