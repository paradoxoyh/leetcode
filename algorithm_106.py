# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            index=inorder.index(postorder.pop())
            root=TreeNode(inorder[index])
            root.right=self.buildTree(inorder[index+1:],postorder)#上下两行顺序不能颠倒
            root.left=self.buildTree(inorder[:index],postorder)
            return root
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #后序序列中root.right-root.left-root,并且是从后序序列中的最后位置pop()
        #所以line13,14顺序如此