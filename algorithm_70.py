class Solution(object):
    def climbStairs(self, n):
        NumofPath=[1,2]
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n):
            temp=NumofPath[i-1]+NumofPath[i-2]
            NumofPath.append(temp)
        return NumofPath[-1]
        """
        :type n: int
        :rtype: int
        """
        