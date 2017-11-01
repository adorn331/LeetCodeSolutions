class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode((l1.val + l2.val) % 10)   #返回的第三条链
        carry = 1 if l1.val + l2.val >= 10 else 0   #储存进位
        l1 = l1.next
        l2 = l2.next
        node = l3
        while l1 and l2: #两条链都不为空的时候对应相加
            node.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = 1 if l1.val + l2.val + carry >= 10 else 0　  #判断是否有进位
            l1 = l1.next
            l2 = l2.next
            node = node.next
        while l1:   #将剩下的那条链与进位相加
            node.next = ListNode((l1.val + carry) % 10)
            carry = 1 if l1.val + carry >= 10 else 0
            l1 = l1.next
            node = node.next
        while l2:
            node.next = ListNode((l2.val + carry) % 10)
            carry = 1 if l2.val + carry >= 10 else 0
            l2 = l2.next
            node = node.next
        if carry:  #最后可能多进一位最高位
            node.next = ListNode(carry)
        return l3