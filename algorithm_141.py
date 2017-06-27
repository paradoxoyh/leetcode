# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            slow=head
            fast=head.next
            while slow!=fast:
                slow=slow.next
                fast=fast.next.next
            return True
        except:
            return False
        """
        :type head: ListNode
        :rtype: bool
        """
        #因为每个节点只有一个next，所以如果存在环那么链表的尾部一定是一个环，先进去的fast就会在里面转圈
        #并且迟早会跟后进入的slow相碰
        #如果不是圈，fast=fast.next.next迟早会报错，return False