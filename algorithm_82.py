# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head==None:
            return []
        cache_val,cache_listnode,tag=[head.val],[head],0
        head=head.next
        while head!=None:
            if head.val==cache_val[0]:
                tag=1
                if head.next==None:
                    cache_listnode.pop(-1)
            elif tag==1:
                cache_listnode.pop(-1)
                tag=0
            if tag==0:
                cache_listnode.append(head)
                cache_val[0]=head.val
            head=head.next
        for i in xrange(len(cache_listnode)-1):
            cache_listnode[i].next=cache_listnode[i+1]
        if cache_listnode==[]:
            return []
        else:
            cache_listnode[-1].next=None
            return cache_listnode[0]
        """
        :type head: ListNode
        :rtype: ListNode
        """