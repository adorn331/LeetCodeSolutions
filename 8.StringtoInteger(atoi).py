class Solution:
    def myAtoi(self, str):
        stripped = str.strip()
        if stripped == '' or not stripped[0].isdigit() and not stripped[0] in '-+':
            return 0    #去掉前导空格并且保证开头第一个是数字或正负号
        for i in range(1, len(stripped)):
            if not stripped[i].isdigit():
                stripped = stripped[:i]
                break       #去掉末尾的不是数字字符
        if stripped != '+' and stripped != '-': #防止最后只剩下+或者-而没有数字
            if -2147483648 <= int(stripped) <= 2147483647:  #防止溢出
                return int(stripped)
            else:
                return 2147483647 if int(stripped) >= 2147483647 else -2147483648
        else:
            return 0