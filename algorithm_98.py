# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        ret=self.dfs(root)
        if type(ret)==type([]):
            return True
        else:
            return ret
    def dfs(self, root):
        if not root:
            return []
        cache_left=self.dfs(root.left)
        cache_right=self.dfs(root.right)
        if type(cache_left)==type([]) and type(cache_right)==type([]):
            if not cache_left:
                bool_left=True
            elif root.val>max(cache_left):
                bool_left=True
            else:
                bool_left=False
            if not cache_right:
                bool_right=True
            elif root.val<min(cache_right):
                bool_right=True
            else:
                bool_right=False
            if bool_left and bool_right:
                cache=cache_left+[root.val]+cache_right
                return cache
            else:
                return False
        else:
            return False
        """
        :type root: TreeNode
        :rtype: bool
        """
        