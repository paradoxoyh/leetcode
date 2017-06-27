class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        miss=list(word)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board,miss,i,j):
                    return True
        return False
    def dfs(self,board,miss,m,n):
        if miss==[]:
            return True
        if n<0 or n>=len(board[0]) or m<0 or m>=len(board) or board[m][n]!=miss[0]:
            return False
        temp=board[m][n]
        board[m][n]='1'
        ret=self.dfs(board,miss[1:],m+1,n) or self.dfs(board,miss[1:],m,n+1) or self.dfs(board,miss[1:],m-1,n) or self.dfs(board,miss[1:],m,n-1)
        board[m][n]=temp
        return ret
         
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #采用递归思想