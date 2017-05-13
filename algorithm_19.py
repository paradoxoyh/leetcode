# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        link=[head]
        while True:
            if link[-1].next!=None:
                link.append(link[-1].next)
            else:
                break
        leng=len(link)
        link.append(None)
        if leng==n:
            return link[1]
        elif n==1:
            link[leng-n-1].next=None
        else:
            link[leng-n-1].next=link[leng-n+1]
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        