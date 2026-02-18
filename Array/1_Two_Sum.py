class Solution(object):
    def twoSum(self, nums, target):
        numvar={}
        for i in range(len(nums)):
            neededvalue=target-nums[i]
            if neededvalue in numvar:
                return [i,numvar[neededvalue]] 
            else:
                numvar[nums[i]]=i
        return [] 
