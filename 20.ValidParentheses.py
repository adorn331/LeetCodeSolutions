class Solution:
    def isValid(self, s):
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if stack and c == pair[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        return False if stack else True

s = Solution(


)

print(s.isValid('[][(]'))