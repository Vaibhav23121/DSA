class Solution(object):
    def searchInsert(self, nums, target):
        upb=len(nums)-1
        lob=0
        while upb>=lob:
            mid=lob+(upb-lob)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                upb=mid-1
            else:
                lob=mid+1
        return upb+1 if nums[mid]<target else lob
