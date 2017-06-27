# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        res=self.dfs(root)
        if res:
            return True
        else:
            return False
    def dfs(self,Root):
        if Root:
            right_level=self.dfs(Root.right)
            left_level=self.dfs(Root.left)
            if right_level and left_level:
                if right_level-left_level<=1 and left_level-right_level<=1:
                    return max(right_level,left_level)+1
                else:
                    return False
            else:
                return False
        else:
            return 1
        """
        :type root: TreeNode
        :rtype: bool
        """
        