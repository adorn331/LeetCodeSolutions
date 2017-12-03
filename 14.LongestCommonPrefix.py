class Solution:
    def longestCommonPrefix(self, strs):
        min_length = min(len(s) for s in strs) if not strs else 0
        if min_length == 0:
            return ''   #if there is '' in strs
        for i in range(min_length):
            if len(set(map(lambda x: x[i], strs))) != 1:
                return strs[0][:i] if i - 1 >= 0 else ''  #dismatch
        return strs[0][:min_length]      #match till min_length