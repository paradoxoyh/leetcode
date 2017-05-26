class Solution(object):
    def totalNQueens(self, n):
        total=set(range(n))
        def dfs(track, level):
            if level==n: return 1
            count=0
            for i in total-set(track):
                if all(level-j!=abs(i-l) for j, l in enumerate(track)): # i like this line in your original code 
                    count+= dfs(track+[i], level+1) # no need to back track 
            return count
        return dfs([], 0)
        """
        :type n: int
        :rtype: int
        """
#使用迭代的方式来对棋盘中的每一行的可能性进行迭代计算
#从第一行的第一种情况开始迭代下一行的情况
#set()，集合函数
#all()，list内不含零，不含null为True
