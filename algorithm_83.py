# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        ret=head
        if ret==None:
            return []
        while head.next!=None:
            temp=head.next
            if temp.val==head.val:
                head.next=None
                if temp.next!=None:
                    head.next=temp.next
            else:
                head=temp
        return ret
        """
        :type head: ListNode
        :rtype: ListNode
        """
        