def orderedGenerator(nums1, nums2):
    #出于空间考虑,这是一个按顺序合并nums1和nums2的generator,不断yield下个两个列表中的最小值
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            yield nums1[i]
            i += 1
        else:
            yield nums2[j]
            j += 1
    while i < len(nums1):
        yield nums1[i]
        i += 1
    while j < len(nums2):
        yield nums2[j]
        j += 1
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        isOdd = len(nums1 + nums2) % 2  #标志是否总长为奇数
        medianCount = len(nums1 + nums2) // 2 + 1 if isOdd else len(nums1 + nums2) // 2 #标志中间的那个数是合并后的第几个
        curCount = 0 #标志当前数到了第几个数
        nums = orderedGenerator(nums1, nums2)
        for num in nums:
            curCount += 1
            if curCount == medianCount:
                return 1.0 * num if isOdd else (num + next(nums)) / 2.0 #若总长不是偶数就要取下个数加起来平均