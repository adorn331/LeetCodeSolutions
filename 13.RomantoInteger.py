class Solution:
    def romanToInt(self, s):
        intMap = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i in range(len(s)):
            minus = False
            for res in s[i:len(s)]:
                if intMap[res] > intMap[s[i]]:
                    minus = True    #只要字符串后面有数值比它大的就说明表示减法
                    break
            ret = ret - intMap[s[i]] if minus else ret + intMap[s[i]]
        return ret