class Solution(object):
    def isValid(self, s):
        s=list(s)
        stack=[]
        s = map(lambda x:[x,-1][x=='('],s)
        s = map(lambda x:[x,-2][x=='['],s)
        s = map(lambda x:[x,-3][x=='{'],s)
        s = map(lambda x:[x,1][x==')'],s)
        s = map(lambda x:[x,2][x==']'],s)
        s = map(lambda x:[x,3][x=='}'],s)
        while s:
            if s[0]<0:
                stack.append(s[0])
            elif stack:
                if s[0]+stack[-1]!=0:
                    return False
                    break
                else:
                    stack.pop(-1)
            else:
                return False
                break
            s.pop(0)
        if stack:
            return False
        else:
            return True
        """
        :type s: str
        :rtype: bool
        """
        