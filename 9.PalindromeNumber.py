class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        tenBase = 1 #用于储存当前数字10的幂次量级,方便后面取头一个数字
        while x / tenBase >= 10:
            tenBase *= 10
        while x:
            head = x // tenBase #开头数字
            tail = x % 10   #尾端数字
            if head != tail:
                return False
            x = x % tenBase // 10
            tenBase /= 100
        return True

