class Solution(object):
    def spiralOrder(self, matrix):
        mat=matrix
        ret=[]
        dirc=[1,2,3,4]
        if mat==[]:
            return ret
        n=len(mat[0])
        m=len(mat)
        if mat==[]:
            return []
        i,j=0,0
        for k in range(n*m):
            ret.append(mat[i][j])
            mat[i][j]=0
            if dirc[0]==1:
                if j+1<=n-1:
                    if mat[i][j+1]!=0:                             
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
                if i+1<=m-1:
                    if mat[i+1][j]!=0:
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
                    if mat[i][j-1]!=0:
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
                    if mat[i-1][j]!=0:
                        i=i-1
                    else:
                        dirc.append(dirc[0])
                        dirc.pop(0)
                        j=j+1
                else:
                    dirc.append(dirc[0])
                    dirc.pop(0)
                    j=j+1
        return ret
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
