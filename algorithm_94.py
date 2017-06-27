# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        ret=[]
        self.dfs(root, ret)
        return ret
    def dfs(self, node, ret):
        if node!=None:
            self.dfs(node.left, ret)
            ret.append(node.val)
            self.dfs(node.right, ret)
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        