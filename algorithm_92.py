# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        cache_node=[]
        while head!=None:
            cache_node.append(head)
            head=head.next
        cache_node[m-1:n]=reversed(cache_node[m-1:n])
        if cache_node!=[]:
            cache_node[-1].next=None
        for i in xrange(len(cache_node)-1):
            cache_node[i].next=cache_node[i+1]
        return cache_node[0]
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        