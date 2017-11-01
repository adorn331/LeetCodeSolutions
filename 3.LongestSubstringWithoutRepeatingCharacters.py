def repeatPos(s):   #返回与尾字符重复的位置，无则返回－１
    for i in s:
        if s.count(i) > 1:
            return s.index(i)
    return -1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        start, end = 0, 1   #子串起始和终止位置
        maxLength = 1
        while end <= len(s):
            fristRepeat = repeatPos(s[start:end])
            if fristRepeat == -1:   #此子串没有重复字符
                maxLength = end - start if end - start > maxLength else maxLength
            else:
                start = start + fristRepeat + 1 #有重复字符则将子串起始位置移动到首个重复处的下一个
            end += 1
        return maxLength