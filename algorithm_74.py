class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            if target>matrix[i][n-1]:
                pass
            else:
                break
        mat=matrix[i]
        for i in mat:
            if i==target:
                return True
                break
        return False   
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        