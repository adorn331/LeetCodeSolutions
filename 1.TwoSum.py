class Solution(object):
    def twoSum(self, nums, target):
        neededDict = dict() #保存之前遍历过的数距离target所差的大小,映射的值为之前之前那些数字的下标
        for i, v in enumerate(nums):
            if v in neededDict:
                return [neededDict[v], i]
            else:
                neededDict[target - v] = i