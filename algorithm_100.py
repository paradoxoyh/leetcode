# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        tree0=[p]
        tree1=[q]
        tag=0
        if q==p==None:
            return True
        elif q==None or p==None:
            return False
        while len(tree0)!=0 and len(tree1)!=0:
            if tree0[0].val!=tree1[0].val:
                return False
                break
            if tree0[0].left!=None:
                tree0.append(tree0[0].left)
                tag+=1
            if tree0[0].right!=None:
                tree0.append(tree0[0].right)
                tag+=10
            if tree1[0].left!=None:
                tree1.append(tree1[0].left)
                tag-=1
            if tree1[0].right!=None:
                tree1.append(tree1[0].right)
                tag-=10
            if tag!=0:
                return False
                break
            tree0.pop(0)
            tree1.pop(0)
        return True
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        