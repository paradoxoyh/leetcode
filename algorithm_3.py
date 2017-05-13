class Solution(object):
    def lengthOfLongestSubstring(self, s):
        Max,slow=0,0
        for i in xrange(len(s)):
            if s[i] in s[slow:i]:
                slow=s[slow:i].index(s[i])+slow+1
            if i-slow+1>Max:
                Max=i-slow+1
        return Max
        """
        :type s: str
        :rtype: int
        """
        