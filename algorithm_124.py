# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        ret=[]
        x=self.dfs(root,ret)
        return max(ret)
    def dfs(self,root,ret):
        if not root:
            return 0
        max_left=self.dfs(root.left,ret)
        max_right=self.dfs(root.right,ret)
        ret.append(max(max_left,0)+max(max_right,0)+root.val)
        return max(max_left,max_right,0)+root.val
        """
        :type root: TreeNode
        :rtype: int
        """
        