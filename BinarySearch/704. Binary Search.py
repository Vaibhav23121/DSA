class Solution(object):
    def search(self, nums, target):
        lb=0
        ub=len(nums)-1
        while lb<=ub:
            mid=lb+(ub-lb)/2
            if target==nums[mid]:
                return mid
            elif nums[mid]>target:
                ub=mid-1
            else:
                lb=mid+1
        return -1
            
