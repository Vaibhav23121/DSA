class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        n=len(nums)
        k=1
        if not nums:
            return 0
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
        
