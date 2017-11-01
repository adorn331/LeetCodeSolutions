class Solution(object):
    def reverse(self, x):
        if x == 0:  #0是特殊情况,因为处理数字的时候会去掉后缀0
            return 0
        ret =  int(str(x).rstrip('0')[::-1]) if x >= 0 else -1 * int(str(x).rstrip('0')[:0:-1])
        return ret if -1 * 2**31 <= ret and ret <= 2**31 - 1 else 0 #防止溢出