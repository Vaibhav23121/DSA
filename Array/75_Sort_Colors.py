class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j]>=nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
        return nums
