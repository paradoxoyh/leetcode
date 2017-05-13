class Solution(object):
    def isPalindrome(self, x):
        ch=str(x)
        ch=list(ch)
        if len(ch)==1:
            return True
        while len(ch)!=1 and len(ch)!=0:
            if ch[0]!=ch[-1]:
                return False
                break
            else:
                ch.pop(0)
                ch.pop(-1)
        return True
        """
        :type x: int
        :rtype: bool
        """
        