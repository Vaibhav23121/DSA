class Solution(object):
    def check(self, nums):
        sorted_nums = sorted(nums)
    
        for i in range(len(nums)):
            rotated = sorted_nums[i:] + sorted_nums[:i]
            if rotated == nums:
                return True
            
        return False
