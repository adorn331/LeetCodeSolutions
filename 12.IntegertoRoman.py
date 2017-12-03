class Solution:
    def intToRoman(self, num):
        toMap = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'VI'), (1, 'I')]
        ret = ''
        while num > 0:
            for i in toMap:
                if num >= i[0]:
                    num -= i[0]
                    ret += i[1]
                    break
        return ret