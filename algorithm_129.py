# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        val=[root.val]
        node_mem=[root]
        sum=[0]
        for i in node_mem:
            if i.left!=None:
                temp=i.left
                node_mem.append(temp)
                val.append(temp.val)
            if i.right!=None:
                temp=i.right
                node_mem.append(temp)
                val.append(temp.val)
        leng=len(val)
        count=0
        i=0
        while leng>=2**count:
            cover=sum[:]
            biase=0
            for j in range(2**count):
                if j%2==0:
                    sum[j]=cover[j/2]*10+val[i]  #####
                else:
                    sum.insert(1+biase,cover[(j-1)/2]*10+val[i])
                    biase=biase+2
                i=i+1
            leng=leng-2**count
            count=count+1
        else:
            cover=sum[:]
            biase=0
            for j in range(leng):
                if j%2==0:
                    sum[j]=cover[j/2]*10+val[i]  #####
                else:
                    sum.insert(1+biase,cover[(j-1)/2]*10+val[i])
                    biase=biase+2
                i=i+1
        return sum
        ret=0
        for i in sum:
            ret=ret+i
        return ret
        """
        :type root: TreeNode
        :rtype: int
        """