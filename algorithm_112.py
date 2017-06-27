# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        tree=[root]
        path=[root.val]
        count=0
        while len(tree)!=0:
            tag=0
            if tree[0].left!=None:
                tag=1
                tree.append(tree[0].left)
                temp=tree[0].left
                path.append(path[count]+temp.val)
            if tree[0].right!=None:
                tag=1
                tree.append(tree[0].right)
                temp=tree[0].right
                path.append(path[count]+temp.val)
            if tag==1:
                path[count]='y'
            tree.pop(0)
            count+=1
        if sum in path:
            return True
        else:
            return False
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        