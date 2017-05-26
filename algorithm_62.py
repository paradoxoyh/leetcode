class Solution(object):
    def uniquePaths(self, m, n):
        if m==1 or  n==1:
            return 1
        def c(n,k):
            num1=1
            num2=1
            for i in range(n-k+1,n+1):
                num1*=i
            for i in range(1,k+1):
                num2*=i
            return num1/num2
        return c(n+m-2,m-1)
        """
        :type m: int
        :type n: int
        :rtype: int
        """
#C(m-1,m+n-2)
#或者使用皇后问题中的迭代思路
