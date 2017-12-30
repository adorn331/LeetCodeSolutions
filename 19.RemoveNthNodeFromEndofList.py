class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        head_bak = head     #备份原链表头用于返回的
        while head:
            length += 1
            head = head.next
        if length == 0 or length == 1:  #表元素个数为1或0
            return None
        if n == length:     #删除头
            return head_bak.next
        head = head_bak
        order_n = length - n - 1
        for i in range(order_n):
            head = head.next
        head.next = head.next.next
        return head_bak