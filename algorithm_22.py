class Solution(object):
    def generateParenthesis(self, n):
        ret=[]
        for i in range(2**(2*n-1),2**(2*n)-1):
            tag=0
            count_0=0
            count_1=0
            x=bin(i)
            for j in x[2:]:
                if j=='1':
                    count_1=count_1+1
                else:
                    count_0=count_0+1
                if count_1<count_0:
                    tag=1
                    break
            if count_1==count_0 and tag==0:
                ret.append(x[2:])
        for i in range(len(ret)):
            ret[i]=list(ret[i])
            for j in range(2*n):
                if ret[i][j]=='1':
                    ret[i][j]='('
                else:
                    ret[i][j]=')'
            ret[i]=''.join(ret[i])
        return ret
        """
        :type n: int
        :rtype: List[str]
        """
        
