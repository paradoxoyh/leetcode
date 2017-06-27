class Solution(object):
    def minDistance(self, word1, word2):
        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))
        word1,word2=list(word1),list(word2)
        mat=[[0 for i in range(1+len(word1))] for j in range(1+len(word2))]
        for i in range(len(word2)+1):
            mat[i][0]=i
        for j in range(len(word1)+1):
            mat[0][j]=j
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    mat[i][j]=mat[i-1][j-1]
                else:
                    mat[i][j]=min(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])+1
        #return mat
        return mat[len(word2)][len(word1)]
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #动态规划思想
        #长度为i,j的两个字符串的距离分情况讨论，word[i]==word[j]
        #等于的话：mat[i][j]=mat[i-1][j-1]
        #不等于的话：mat[i][j]=min(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])+1
        #return mat[-1][-1]