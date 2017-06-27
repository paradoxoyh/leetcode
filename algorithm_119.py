class Solution(object):
    def getRow(self, rowIndex):
        res = [[1]]
        for i in range(1, rowIndex+1):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[-1]
        
        """
        :type rowIndex: int
        :rtype: List[int]
        """