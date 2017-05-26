class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n,O=len(obstacleGrid),len(obstacleGrid[0]),obstacleGrid
        num=[[0 for j in range(n)] for i in range(m)]
        if O[0][0]==0:
            num[0][0]=1
        else:
            num[0][0]=0
        for i in range(m):
            for j in range(n):
                if O[i][j]==0:
                    if i-1>=0:
                        num[i][j]+=num[i-1][j]
                    if j-1>=0:
                        num[i][j]+=num[i][j-1]
        return num[m-1][n-1]
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
