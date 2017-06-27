class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
        #非环的长度为H，环的长度为L。按照algorithm_141的算法，假设fast与slow在距离环的起点的D处相遇：
        #slow走的距离为H+D，fast走的距离为2H+2D,于是fast-slow=nL  =>   H+D=nL
        #所以对于slow来说，已经走了H+D，那么继续往前走H时，就有H+D+H=H+D+(nL-D)=H+nL  正好停留在环的起点处