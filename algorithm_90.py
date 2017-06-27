class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res
        #排序，保证重复的数字在一起出现
        #如果跟前一个数字不相同，那么新的集合就变成原有的集合+添加了该元素的新集合
        #如果相同，则上一次扩展的集合添加上该元素组成新的集合，因为再之前的已经添加过该元素