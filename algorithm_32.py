class Solution(object):
    def longestValidParentheses(self, s):
        if len(s)<2:
            return 0
        res_pos=self.subfunc(s,'(')
        res_nag=self.subfunc(s[::-1],')')
        return max(res_pos,res_nag)
    def subfunc(self,s,a):
        value=[1]
        S=[]
        for i in xrange(len(s)):
            if s[i]==a:
                S=s[i:]
                break
        for i in xrange(1,len(S)):
            if S[i]==a:
                value.append(value[-1]+1)
            else:
                value.append(value[-1]-1)
        res=0
        temp=[0]
        for i in value[1:]:
            if i>=temp[0]:
                temp.append(i)
                if i==temp[0]:
                    res=max(res,len(temp))
            else:
                res=max(res,len(temp))
                if i>temp[-1]:
                    temp=[i-1]
                else:
                    temp=[100000,i]
        return res
        """
        :type s: str
        :rtype: int
        ""“      
