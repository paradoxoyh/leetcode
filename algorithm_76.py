class Solution(object):
    def minWindow(self, s, t):
        miss=list(t)
        dic={}
        end=len(s)
        start=0
        for char in t:
            dic[char]=[]
        for i in range(len(s)):
            if s[i] in t:
                if s[i] in miss:
                    miss.remove(s[i])
                elif s[i] not in miss and dic[s[i]]!=[]:
                    dic[s[i]].pop(0)
                dic[s[i]].append(i)
            if miss==[]:
                maximum=max([dic[x][-1] for x in dic])
                minimum=min([dic[x][0] for x in dic])
                if maximum-minimum<end-start:
                    end=maximum
                    start=minimum
        if miss!=[]:
            return ""
        else:
            return s[start:end+1]
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        