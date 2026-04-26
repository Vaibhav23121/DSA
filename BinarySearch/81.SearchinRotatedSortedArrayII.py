import numpy as np
class Solution(object):
    def search(self, nums, target):
        nums=np.asarray(nums)
        nums=np.unique(nums)
        ub=len(nums)-1
        lb=0
        while(ub>=lb):
            mid=lb+(ub-lb)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                ub=mid-1
            else:
                lb=mid+1
        return False

        
