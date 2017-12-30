class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ret = []
        for o in range(len(nums) - 2):
            for i in range(o + 1, len(nums) - 2):
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] + nums[o] == target:
                        if not (ret and [nums[o], nums[i], nums[j], nums[k]] == ret[-1]):
                            ret.append([nums[o], nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[o] < target:
                        j += 1
                    else:
                        k -= 1
        return ret

s = Solution()
print(s.fourSum([-3,-3,-1,0,2, 4,5], 1))

