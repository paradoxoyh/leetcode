class Solution(object):
    def wordBreak(self, s, wordDict):
        length=len(s)
        ret=[False for i in s]
        for i in xrange(length):
            for j in wordDict:
                if s[i-len(j)+1:i+1]==j and (ret[i-len(j)] or i-len(j)+1==0):
                    ret[i]=True
        return ret[-1]
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #DP思想，M的值由N的值以及[N+1:M]与wordDict的比较结果决定