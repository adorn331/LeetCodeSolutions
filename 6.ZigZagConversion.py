def mergeStr(headStr, followStr):   #穿插合并两个字符串,例如'123' 和 'abc' 合并为'1a2b3c'
    if len(followStr) == 0:
        return headStr
    ret = ''
    for i, j in zip(headStr, followStr):
        ret += i + j
    if len(headStr) != len(followStr):
        ret += headStr[-1] if len(headStr) > len(followStr) else followStr[-1]
    return ret
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        ret = ''
        step = 2 * numRows - 2
        for i in range(numRows):
            verticalPart = s[i::step]   #排列的时候出于锯齿状的竖直部分的字符
            inclinePart = s[step - i::step] if i != 0 and i != numRows - 1 else '' #排列的时候出于锯齿状的倾斜部分的字符
            ret += mergeStr(verticalPart, inclinePart)  #因为从左向右扫描合成新字符串,故merge
        return ret