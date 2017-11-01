class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        ispalindrome = lambda x: x == x[::-1]
        ret = s[0]
        length = len(s)
        front, rear = 0, 1
        while front < length - len(ret):
            while rear < length and s[rear] != s[front]:
                rear += 1
            if not rear < length:
                front += 1
                rear = front + 1
                continue
            if rear - front + 1 > len(ret) and ispalindrome(s[front:rear + 1]):
                ret = s[front:rear + 1]
            rear += 1
        return ret