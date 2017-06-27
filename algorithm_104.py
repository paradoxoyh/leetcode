# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        tree=[root]
        num=[1]
        count=0
        if root==None:
            return 0
        while len(tree)!=0:
            tag=0
            if tree[0].left!=None:
                tree.append(tree[0].left)
                num.append(num[count]+1)
            if tree[0].right!=None:
                tree.append(tree[0].right)
                num.append(num[count]+1)
            tree.pop(0)
            count+=1
        return max(num)
        """
        :type root: TreeNode
        :rtype: int
        """
        