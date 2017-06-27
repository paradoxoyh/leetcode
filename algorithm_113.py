# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, Sum):
        if not root:
            return []
        res=[[root.val]]
        ret=[]
        cache_node=[root]
        while cache_node:
            if cache_node[0].left or cache_node[0].right:
                if cache_node[0].left:
                    cache_node.append(cache_node[0].left)
                    res.append(res[0]+[cache_node[0].left.val])
                if cache_node[0].right:
                    cache_node.append(cache_node[0].right)
                    res.append(res[0]+[cache_node[0].right.val])
            else:
                ret.append(res[0])
            res.pop(0)
            cache_node.pop(0)
        i=0
        while i!=len(ret):
            if sum(ret[i])!=Sum:
                ret.pop(i)
            else:
                i+=1
        return ret
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        