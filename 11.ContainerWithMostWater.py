class Solution:
    def maxArea(self, height):
        ret, front, rear = 0, 0, len(height) - 1
        while front < rear:
            area = (rear - front) * min(height[front], height[rear])
            ret = area if area > ret else ret
            if height[front] < height[rear]:
                front += 1
            else:
                rear -= 1
        return ret

# class Solution:
#     def maxArea(self, height):
#         ret= 0
#         for i, curH in enumerate(height):
#             if curH * max(i, len(height) - i) > ret:
#                 for j in list(range(i)) + list(range(i + 1, len(height))):
#                     if height[j] >= curH and abs(i - j) * curH > ret:
#                         ret = abs(i - j) * curH
#         return ret
