# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        min=1
        max=n
        if max==min+1:
            tag=guess(max)
            if tag==0:
                return max
            else:
                return min
        if (max-min)%2==0:
            mid=(max-min)/2+min
            tag=guess(mid)
        else:
            mid=((max-min)+1)/2
            tag=guess(mid)
        while tag!=0:
            if max==min+1:
                tag=guess(max)
                if tag==0:
                    return max
                    break
                else:
                    return min
                    break
            if tag==1:
                min=mid
            else:
                max=mid
            if (max-min)%2==0:
                mid=(max-min)/2+min
                tag=guess(mid)
            else:
                mid=((max-min)+1)/2+min
                tag=guess(mid)
        else:
            return mid
        """
        :type n: int
        :rtype: int
        """
        