# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        local,cache_node=0,[]
        while head!=None:
            if head.val>=x:
                cache_node.append(head)
            else:
                cache_node.insert(local,head)
                local+=1
            head=head.next
        if cache_node!=[]:
            cache_node[-1].next=None
        for i in xrange(len(cache_node)-1):
            cache_node[i].next=cache_node[i+1]
        return cache_node[0]
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        