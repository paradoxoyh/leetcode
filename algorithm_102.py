# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        mark,ret,cache=1,[],[root]
        while cache:
            ret.append([])
            temp=0
            for i in xrange(mark):
                if cache[0].left:
                    cache.append(cache[0].left)
                else:
                    temp+=1
                if cache[0].right:
                    cache.append(cache[0].right)
                else:
                    temp+=1
                ret[-1].append(cache[0].val)
                cache.pop(0)
            mark=mark*2-temp
        return ret
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """