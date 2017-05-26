class Solution(object):
    def generateMatrix(self, n):
        mat=[[0 for i in range(n)] for j in range(n)]
        dirc=[1,2,3,4]
        i,j=0,0
        if n==0:
            return []
        for k in range(1,n**2+1):
            mat[i][j]=k
            if dirc[0]==1:
                if j+1<=n-1:
                    if mat[i][j+1]==0: 
                        j=j+1
                    else:
                        dirc.append(dirc[0])
                        dirc.pop(0)
                        i=i+1
                else:
                    dirc.append(dirc[0])
                    dirc.pop(0)
                    i=i+1
            elif dirc[0]==2:
                if i+1<=n-1:
                    if mat[i+1][j]==0:
                        i=i+1
                    else:
                        dirc.append(dirc[0])
                        dirc.pop(0)
                        j=j-1
                else:
                    dirc.append(dirc[0])
                    dirc.pop(0)
                    j=j-1
            elif dirc[0]==3:
                if j-1>=0:
                    if mat[i][j-1]==0:
                        j=j-1
                    else:
                        dirc.append(dirc[0])
                        dirc.pop(0)
                        i=i-1
                else:
                    dirc.append(dirc[0])
                    dirc.pop(0)
                    i=i-1
            else:
                if i-1>=0:
                    if mat[i-1][j]==0:
                        i=i-1
                    else:
                        dirc.append(dirc[0])
                        dirc.pop(0)
                        j=j+1
                else:
                    dirc.append(dirc[0])
                    dirc.pop(0)
                    j=j+1
        return mat
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
