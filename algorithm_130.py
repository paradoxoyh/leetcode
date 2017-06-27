class Solution(object):
    def solve(self, board):
        if not board: 
            return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']
    #利用一个队列保存激活节点
    #最初始的激活节点为边界上的'O'节点，并且将其四周为'O'的节点作为激活节点put到队列中