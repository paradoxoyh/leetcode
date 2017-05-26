class Solution(object):
    def mySqrt(self, x):
        y=x
        mi=[1]
        if x==1:
            return 1
        while True:
            if x>mi[-1]:
                x=x>>1
                mi.append(mi[-1]*2)
            else: 
                break
        if len(mi)>1:
            for i in range(mi[-2],mi[-1]+2):
                if i**2>y:
                    return i-1
                    break
        else:
            return mi[0]-1
        """
        :type x: int
        :rtype: int
        """
        
