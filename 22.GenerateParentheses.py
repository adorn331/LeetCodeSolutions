class Solution:
    def generateParenthesis(self, n):
        res = []
        if n == 0:
            res.append("")
            return res
        elif n == 1:
            res.append("()")
            return res
        for i in range(n):
            front = self.generateParenthesis(i)
            rear = self.generateParenthesis(n - i - 1)
            for r in rear:
                for f in front:
                    res.append('(' + f + ')' + r)
        return res

s = Solution()
print(s.generateParenthesis(3))