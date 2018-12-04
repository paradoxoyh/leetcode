class Solution(object):
    def longestCommonPrefix(self, strs):
        k = 0
        [minLength, minIndex] = self.shortestStr(strs)
        if(minLength == 0):
            return ""
        while(strs and strs[0][:]):
            singleC = strs[minIndex][k]
            for i in range(len(strs)):
                if strs[i][k] != singleC:
                    return strs[i][0:k]
            k = k + 1
            if k == (len(strs[minIndex])):
                return strs[minIndex][:]
        return ""
    def shortestStr(self, strs):
        minLength = 2**31;
        minIndex = 0;
        for i in range(len(strs)):
            if minLength > len(strs[i]):
                minIndex = i;
                minLength = len(strs[i])
        return [minLength, minIndex]
        """
        :type strs: List[str]
        :rtype: str
        """
        
