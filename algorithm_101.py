# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        cache_left=[root.left]
        cache_right=[root.right]
        while cache_left and cache_right:
            if cache_left[0] and cache_right[0]:
                if cache_left[0].val!=cache_right[0].val:
                    return False
                    break
                cache_left.append(cache_left[0].left)
                cache_left.append(cache_left[0].right)
                cache_right.append(cache_right[0].right)
                cache_right.append(cache_right[0].left)
            elif cache_left[0] or cache_right[0]:
                return False
                break
            cache_left.pop(0)
            cache_right.pop(0)
        if cache_left or cache_right:
            return False
        return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        