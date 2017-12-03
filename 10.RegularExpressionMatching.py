class Solution:
    def isMatch(self, s, p):
        j, i = 0, 0
        for i in range(len(p)):
            if j >= len(s): #pattern比s长
                if p[i] == '*' and p[i:len(p):2] == '*' * len(p[i:len(p):2]):
                    return True
                if i+1<len(p) and p[-1] == '*' and p[i+1] == '*' and p[i+1:len(p):2] == '*' * len(p[i+1:len(p):2]):
                    return True
                return False
            if p[i] not in ('.', '*'):  #普通字符
                if s[j] == p[i]:
                    j += 1
                else:
                    if i + 1 < len(p) and p[i + 1] == '*': #虽然字符不匹配但p下一个是*,可以跳过
                        continue
                    return False    #单个字符的失配
            elif p[i] == '.':   #可以匹配任何字符
                j += 1
            elif p[i] == '*':
                if p[i - 1] == '.': #上一个是.默认则可以匹配完s
                    return True if i == len(p) - 1 else False
                else:
                    while s[j] == p[i - 1]: #上一个是普通字符可以匹配多个*前面的字符
                        j += 1
                        if j == len(s):
                            return True
        return True if j == len(s) else False

s = Solution()
print(s.isMatch('bbbba', '.*a*a'))