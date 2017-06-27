# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            index=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[index])
            root.left=self.buildTree(preorder,inorder[:index])
            root.right=self.buildTree(preorder,inorder[index+1:])
            return root
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #前序序列中：root-root.left-root.right,所以line13,14顺序如此
        #利用递归方法，中序序列中，root节点左边的值都是其左子树的中序序列
        #一个节点的右边的值都是其右子树中的中序序列