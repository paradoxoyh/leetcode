# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        return self.dfs(root, 1)
    def dfs(self, root, level):
        if not root:
            return level-1
        if root.left and root.right:
            return min(self.dfs(root.left, level+1),self.dfs(root.right, level+1))
        else:
            return max(self.dfs(root.left, level+1),self.dfs(root.right, level+1))
        """
        :type root: TreeNode
        :rtype: int
        """
        