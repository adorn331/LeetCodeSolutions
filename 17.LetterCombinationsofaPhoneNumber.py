class Solution(object):
    def letterCombinations(self, digits):
        num_mapping = {'1': '', '2': 'abc', '3': 'def',
                   '4': 'ghi', '5': 'jkl', '6': 'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
                   '0': ' '}
        ret = [''] if digits else []
        for num in digits:
            ret = [pre + tail for pre in ret for tail in num_mapping[num]]
        return ret
