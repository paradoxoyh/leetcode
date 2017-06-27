class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        num=[1]*n
        num[0]=0
        num[1]=0
        i=2
        while i<n:
            if num[i]==1:
                for j in xrange(2*i,n,i):
                    num[j]=0
            i+=1
        return sum(num)
        """
        :type n: int
        :rtype: int
        """
        