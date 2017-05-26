# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head==None:
            return None
        link=[head]
        while link[-1].next!=None:
            link.append(link[-1].next)
        k=k%len(link)
        link[-1].next=link[0]
        link[-k-1].next=None
        return link[-k]
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
