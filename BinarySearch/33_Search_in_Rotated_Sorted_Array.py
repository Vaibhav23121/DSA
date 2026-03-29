class Solution(object):
    def search(self, nums, target):
        lb=0
        ub=len(nums)-1
        while lb <= ub:
            mid=(ub+lb)//2
            if nums[mid]== target:
                return mid
            if nums[mid]>=nums[lb]:
                if (nums[mid]>=target and target>=nums[lb]):
                    ub=mid-1
                else:
                    lb=mid+1
            else:
                if target>nums[mid] and nums[ub]>=target:
                    lb=mid+1
                else:
                    ub=mid-1
        return -1
