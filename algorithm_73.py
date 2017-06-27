class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]==0:
                    for x in xrange(m):
                        if matrix[x][j]!=0:
                            matrix[x][j]='a'
                    for y in xrange(n):
                        if matrix[i][y]!=0:
                            matrix[i][y]='a'
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]=='a':
                    matrix[i][j]=0
        
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """